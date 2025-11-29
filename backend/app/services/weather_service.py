import httpx
from typing import Any
from app.core.config import settings
from app.schemas.weather import WeatherResponse, LocationData
from app.services.cache_service import CacheService
from app.services.exceptions import GeocodingError, ExternalAPIError


class WeatherService:
    """Service layer for weather data operations."""

    def __init__(self, client: httpx.AsyncClient | None = None):
        self.cache = CacheService()
        self.client = client or httpx.AsyncClient(timeout=10.0)

    async def get_weather_by_city(self, city: str) -> WeatherResponse:
        """
        Fetch weather data for a given city.

        Steps:
        1. Check cache
        2. Geocode city to coordinates
        3. Fetch weather data
        4. Transform and cache response
        """
        cache_key = f"weather:{city.lower()}"

        cached_data = await self.cache.get(cache_key)
        if cached_data:
            return WeatherResponse(**cached_data)

        location = await self._geocode_city(city)

        weather_data = await self._fetch_weather(location.latitude, location.longitude)

        try:
            current = weather_data["current"]
        except Exception as e:
            raise ExternalAPIError("Unexpected weather payload from upstream") from e

        response = WeatherResponse(
            city=location.name,
            country=location.country,
            latitude=location.latitude,
            longitude=location.longitude,
            temperature=current["temperature_2m"],
            apparent_temperature=current["apparent_temperature"],
            humidity=current["relative_humidity_2m"],
            precipitation=current["precipitation"],
            rain=current.get("rain", 0.0),
            wind_speed=current["wind_speed_10m"],
            wind_direction=current["wind_direction_10m"],
            cloud_cover=current["cloud_cover"],
            pressure=current["surface_pressure"],
            weather_code=current["weather_code"],
            timestamp=current["time"],
        )

        await self.cache.set(cache_key, response.model_dump(), ttl=settings.CACHE_TTL_SECONDS)

        return response

    async def _geocode_city(self, city: str) -> LocationData:
        """Convert city name to coordinates using Open-Meteo Geocoding API"""
        resp = await self.client.get(
            f"{settings.GEOCODING_BASE_URL}/search",
            params={"name": city, "count": 1, "language": "en", "format": "json"},
        )

        if resp.status_code != 200:
            raise GeocodingError(f"Failed to geocode city: {city}")

        data = resp.json()

        if not data.get("results"):
            raise GeocodingError(f"City not found: {city}")

        result = data["results"][0]
        return LocationData(
            name=result.get("name", city),
            country=result.get("country", "Unknown"),
            latitude=float(result["latitude"]),
            longitude=float(result["longitude"]),
        )

    async def _fetch_weather(self, latitude: float, longitude: float) -> dict[str, Any]:
        """Fetch weather data from Open-Meteo API"""
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": [
                "temperature_2m",
                "apparent_temperature",
                "relative_humidity_2m",
                "precipitation",
                "rain",
                "cloud_cover",
                "surface_pressure",
                "wind_speed_10m",
                "wind_direction_10m",
                "weather_code",
            ],
            "timezone": "auto",
        }

        resp = await self.client.get(f"{settings.OPEN_METEO_BASE_URL}/forecast", params=params)

        if resp.status_code != 200:
            raise ExternalAPIError("Failed to fetch weather data from Open-Meteo API")

        return resp.json()
