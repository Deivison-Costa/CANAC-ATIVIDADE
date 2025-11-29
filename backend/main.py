from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import httpx

from app.api.routes import weather_router
from app.core.config import settings
from app.services.weather_service import WeatherService
from app.services.exceptions import WeatherServiceError


app = FastAPI(
    title="Weather API for Sugarcane Monitoring",
    description="API wrapper for Open-Meteo weather data",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(weather_router, prefix=settings.API_V1_STR, tags=["weather"])


@app.on_event("startup")
async def startup_event():
    app.state.httpx_client = httpx.AsyncClient(timeout=10.0)
    app.state.weather_service = WeatherService(client=app.state.httpx_client)


@app.on_event("shutdown")
async def shutdown_event():
    client = getattr(app.state, "httpx_client", None)
    if client is not None:
        await client.aclose()


@app.exception_handler(WeatherServiceError)
async def weather_service_error_handler(request: Request, exc: WeatherServiceError):
    return JSONResponse(status_code=502, content={"detail": str(exc)})


@app.get("/")
async def root():
    return {"message": "Weather API for Sugarcane Monitoring", "docs": "/docs", "version": "1.0.0"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
