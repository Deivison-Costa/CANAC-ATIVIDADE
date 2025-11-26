from fastapi import APIRouter, HTTPException, Query
from app.services.weather_service import WeatherService
from app.schemas.weather import WeatherResponse

weather_router = APIRouter()
weather_service = WeatherService()


@weather_router.get("/weather", response_model=WeatherResponse)
async def get_weather(city: str = Query(..., description="City name to get weather for")):
    """
    Get current weather data for a given city.

    This endpoint acts as a wrapper for the Open-Meteo API,
    providing weather information relevant for sugarcane farming.
    """
    try:
        weather_data = await weather_service.get_weather_by_city(city)
        return weather_data
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
