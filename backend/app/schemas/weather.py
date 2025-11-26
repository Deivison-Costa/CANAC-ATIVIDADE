from pydantic import BaseModel, Field


class LocationData(BaseModel):
    """Location information from geocoding"""

    name: str
    country: str
    latitude: float
    longitude: float


class WeatherResponse(BaseModel):
    """Weather response model optimized for sugarcane farming"""

    city: str = Field(..., description="City name")
    country: str = Field(..., description="Country")
    latitude: float = Field(..., description="Latitude")
    longitude: float = Field(..., description="Longitude")

    temperature: float = Field(..., description="Current temperature in Celsius")
    apparent_temperature: float = Field(..., description="Feels like temperature in Celsius")

    humidity: int = Field(..., description="Relative humidity in %")
    precipitation: float = Field(..., description="Total precipitation in mm")
    rain: float = Field(..., description="Rain in mm")

    wind_speed: float = Field(..., description="Wind speed in km/h")
    wind_direction: int = Field(..., description="Wind direction in degrees")

    cloud_cover: int = Field(..., description="Cloud cover in %")
    pressure: float = Field(..., description="Surface pressure in hPa")
    weather_code: int = Field(..., description="WMO Weather code")
    timestamp: str = Field(..., description="Timestamp of the data")

    class Config:
        json_schema_extra = {
            "example": {
                "city": "São Paulo",
                "country": "Brazil",
                "latitude": -23.5505,
                "longitude": -46.6333,
                "temperature": 25.5,
                "apparent_temperature": 27.0,
                "humidity": 65,
                "precipitation": 0.0,
                "rain": 0.0,
                "wind_speed": 15.2,
                "wind_direction": 180,
                "cloud_cover": 40,
                "pressure": 1013.5,
                "weather_code": 1,
                "timestamp": "2024-01-15T14:30:00",
            }
        }
