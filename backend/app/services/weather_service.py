import httpx
from app.core.config import settings
from app.schemas.weather import WeatherResponse, LocationData
from app.services.cache_service import CacheService


class WeatherService:
    """Service layer for weather data operations"""

    def __init__(self):
        self.cache = CacheService()

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

        cached_data = self.cache.get(cache_key)
        if cached_data:
            return WeatherResponse(**cached_data)

        location = await self._geocode_city(city)

        weather_data = await self._fetch_weather(location.latitude, location.longitude)

        response = WeatherResponse(
            city=location.name,
            country=location.country,
            latitude=location.latitude,
            longitude=location.longitude,
            temperature=weather_data["current"]["temperature_2m"],
            apparent_temperature=weather_data["current"]["apparent_temperature"],
            humidity=weather_data["current"]["relative_humidity_2m"],
            precipitation=weather_data["current"]["precipitation"],
            rain=weather_data["current"]["rain"],
            wind_speed=weather_data["current"]["wind_speed_10m"],
            wind_direction=weather_data["current"]["wind_direction_10m"],
            cloud_cover=weather_data["current"]["cloud_cover"],
            pressure=weather_data["current"]["surface_pressure"],
            weather_code=weather_data["current"]["weather_code"],
            timestamp=weather_data["current"]["time"],
        )

        self.cache.set(cache_key, response.model_dump(), ttl=settings.CACHE_TTL_SECONDS)

        return response

    async def _geocode_city(self, city: str) -> LocationData:
        """Convert city name to coordinates using Open-Meteo Geocoding API"""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.GEOCODING_BASE_URL}/search",
                params={"name": city, "count": 1, "language": "en", "format": "json"},
            )

            if response.status_code != 200:
                raise ValueError(f"Failed to geocode city: {city}")

            data = response.json()

            if not data.get("results"):
                raise ValueError(f"City not found: {city}")

            result = data["results"][0]
            return LocationData(
                name=result["name"],
                country=result.get("country", "Unknown"),
                latitude=result["latitude"],
                longitude=result["longitude"],
            )

    async def _fetch_weather(self, latitude: float, longitude: float) -> dict:
        """Fetch weather data from Open-Meteo API"""
        async with httpx.AsyncClient() as client:
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

            response = await client.get(f"{settings.OPEN_METEO_BASE_URL}/forecast", params=params)

            if response.status_code != 200:
                raise Exception("Failed to fetch weather data from Open-Meteo API")

            return response.json()
