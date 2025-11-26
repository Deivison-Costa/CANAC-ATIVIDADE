from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import weather_router
from app.core.config import settings

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

app.include_router(weather_router, prefix="/api/v1", tags=["weather"])


@app.get("/")
async def root():
    return {"message": "Weather API for Sugarcane Monitoring", "docs": "/docs", "version": "1.0.0"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
