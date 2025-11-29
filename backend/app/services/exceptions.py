class WeatherServiceError(Exception):
    """Base exception for weather service errors."""


class GeocodingError(WeatherServiceError):
    """Raised when geocoding fails or city not found."""


class ExternalAPIError(WeatherServiceError):
    """Raised when a downstream API (Open-Meteo) fails."""
