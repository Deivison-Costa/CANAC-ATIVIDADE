import pytest
from app.services.weather_service import WeatherService
from app.schemas.weather import LocationData


@pytest.mark.asyncio
async def test_get_weather_by_city_cache_and_flow(monkeypatch):
    svc = WeatherService()

    async def fake_geocode(self, city: str):
        return LocationData(name="TestCity", country="TestLand", latitude=1.0, longitude=2.0)

    async def fake_fetch(self, lat: float, lon: float):
        return {
            "current": {
                "temperature_2m": 25.0,
                "apparent_temperature": 26.0,
                "relative_humidity_2m": 60,
                "precipitation": 0.0,
                "rain": 0.0,
                "wind_speed_10m": 10.0,
                "wind_direction_10m": 180,
                "cloud_cover": 20,
                "surface_pressure": 1012.0,
                "weather_code": 1,
                "time": "2025-01-01T12:00:00",
            }
        }

    monkeypatch.setattr(svc, "_geocode_city", fake_geocode.__get__(svc, WeatherService))
    monkeypatch.setattr(svc, "_fetch_weather", fake_fetch.__get__(svc, WeatherService))

    r = await svc.get_weather_by_city("TestCity")
    assert r.city == "TestCity"

    r2 = await svc.get_weather_by_city("TestCity")
    assert r2.city == "TestCity"
