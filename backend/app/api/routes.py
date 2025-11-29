from fastapi import APIRouter, HTTPException, Query, Depends, Request
from fastapi import status
from app.schemas.weather import WeatherResponse
from app.services.weather_service import WeatherService
from app.services.exceptions import GeocodingError, ExternalAPIError


weather_router = APIRouter()


async def get_weather_service(request: Request) -> WeatherService:
    """Dependency that returns the application singleton WeatherService."""
    svc: WeatherService | None = getattr(request.app.state, "weather_service", None)
    if svc is None:
        return WeatherService()
    return svc


@weather_router.get("/weather", response_model=WeatherResponse)
async def get_weather(
    city: str = Query(
        ...,
        min_length=2,
        max_length=80,
        description="City name to get weather for",
        pattern=r"^[A-Za-zÀ-ÖØ-öø-ÿ\s\-']+$",
    ),
    weather_service: WeatherService = Depends(get_weather_service),
):
    """
    Get current weather data for a given city.
    """
    try:
        weather_data = await weather_service.get_weather_by_city(city)
        return weather_data
    except GeocodingError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ExternalAPIError as e:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}",
        )
