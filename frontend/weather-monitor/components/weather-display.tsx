import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import {
  Thermometer,
  Droplets,
  Wind,
  CloudRain,
  Cloud,
  Gauge,
  MapPin,
  Calendar,
  Eye,
  Compass,
} from "lucide-react";
import type { WeatherData } from "@/lib/types";
import { getWeatherDescription } from "@/lib/weather-codes";

interface WeatherDisplayProps {
  data: WeatherData;
}

export function WeatherDisplay({ data }: WeatherDisplayProps) {
  const weatherDescription = getWeatherDescription(data.weather_code);

  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-700">
      <Card className="bg-linear-to-br from-primary to-primary/80 text-primary-foreground shadow-xl border-0 overflow-hidden">
        <CardHeader className="pb-6">
          <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-6">
            <div className="flex-1">
              <CardTitle className="text-3xl md:text-4xl font-bold mb-3 text-balance">
                {data.city}, {data.country}
              </CardTitle>
              <div className="flex items-center gap-2 text-sm opacity-90 mb-4">
                <MapPin className="h-4 w-4" />
                <span>
                  {data.latitude.toFixed(4)}°, {data.longitude.toFixed(4)}°
                </span>
              </div>
              <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary-foreground/15 backdrop-blur-sm">
                <Eye className="h-4 w-4" />
                <span className="text-sm font-medium">
                  {weatherDescription}
                </span>
              </div>
            </div>
            <div className="text-center md:text-right">
              <div className="text-6xl md:text-7xl font-bold tracking-tight mb-2">
                {Math.round(data.temperature)}°
              </div>
              <div className="text-base opacity-90">
                Feels like {Math.round(data.apparent_temperature)}°C
              </div>
            </div>
          </div>
        </CardHeader>
      </Card>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6">
        <Card className="hover:shadow-lg transition-shadow duration-300">
          <CardHeader className="pb-3">
            <CardTitle className="text-sm font-semibold flex items-center gap-2 text-muted-foreground uppercase tracking-wide">
              <div className="p-2 rounded-lg bg-chart-1/10">
                <Thermometer className="h-4 w-4 text-chart-1" />
              </div>
              Temperature
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold">
              {data.temperature.toFixed(1)}°C
            </div>
            <p className="text-sm text-muted-foreground mt-2">
              Apparent: {data.apparent_temperature.toFixed(1)}°C
            </p>
          </CardContent>
        </Card>

        <Card className="hover:shadow-lg transition-shadow duration-300">
          <CardHeader className="pb-3">
            <CardTitle className="text-sm font-semibold flex items-center gap-2 text-muted-foreground uppercase tracking-wide">
              <div className="p-2 rounded-lg bg-chart-2/10">
                <Droplets className="h-4 w-4 text-chart-2" />
              </div>
              Humidity
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold">{data.humidity}%</div>
            <p className="text-sm text-muted-foreground mt-2">
              {data.humidity > 70
                ? "High moisture"
                : data.humidity > 40
                  ? "Moderate"
                  : "Low moisture"}
            </p>
          </CardContent>
        </Card>

        <Card className="hover:shadow-lg transition-shadow duration-300">
          <CardHeader className="pb-3">
            <CardTitle className="text-sm font-semibold flex items-center gap-2 text-muted-foreground uppercase tracking-wide">
              <div className="p-2 rounded-lg bg-chart-3/10">
                <CloudRain className="h-4 w-4 text-chart-3" />
              </div>
              Precipitation
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold">{data.rain.toFixed(1)} mm</div>
            <p className="text-sm text-muted-foreground mt-2">
              Total: {data.precipitation.toFixed(1)} mm
            </p>
          </CardContent>
        </Card>

        <Card className="hover:shadow-lg transition-shadow duration-300">
          <CardHeader className="pb-3">
            <CardTitle className="text-sm font-semibold flex items-center gap-2 text-muted-foreground uppercase tracking-wide">
              <div className="p-2 rounded-lg bg-chart-4/10">
                <Wind className="h-4 w-4 text-chart-4" />
              </div>
              Wind Speed
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold">
              {data.wind_speed.toFixed(1)} km/h
            </div>
            <div className="flex items-center gap-2 mt-2">
              <Compass className="h-4 w-4 text-muted-foreground" />
              <p className="text-sm text-muted-foreground">
                {data.wind_direction}° ({getWindDirection(data.wind_direction)})
              </p>
            </div>
          </CardContent>
        </Card>

        <Card className="hover:shadow-lg transition-shadow duration-300">
          <CardHeader className="pb-3">
            <CardTitle className="text-sm font-semibold flex items-center gap-2 text-muted-foreground uppercase tracking-wide">
              <div className="p-2 rounded-lg bg-chart-5/10">
                <Cloud className="h-4 w-4 text-chart-5" />
              </div>
              Cloud Cover
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold">{data.cloud_cover}%</div>
            <p className="text-sm text-muted-foreground mt-2">
              {data.cloud_cover > 70
                ? "Mostly cloudy"
                : data.cloud_cover > 30
                  ? "Partly cloudy"
                  : "Clear skies"}
            </p>
          </CardContent>
        </Card>

        <Card className="hover:shadow-lg transition-shadow duration-300">
          <CardHeader className="pb-3">
            <CardTitle className="text-sm font-semibold flex items-center gap-2 text-muted-foreground uppercase tracking-wide">
              <div className="p-2 rounded-lg bg-muted">
                <Gauge className="h-4 w-4 text-foreground" />
              </div>
              Pressure
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold">
              {data.pressure.toFixed(1)} hPa
            </div>
            <p className="text-sm text-muted-foreground mt-2">
              Surface pressure
            </p>
          </CardContent>
        </Card>
      </div>

      <Card className="border-2 border-dashed">
        <CardContent className="py-4">
          <div className="flex items-center justify-center gap-2 text-sm text-muted-foreground">
            <Calendar className="h-4 w-4" />
            <span className="font-medium">Last updated:</span>
            <span>{new Date(data.timestamp).toLocaleString()}</span>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

function getWindDirection(degrees: number): string {
  const directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"];
  const index = Math.round((degrees % 360) / 45) % 8;
  return directions[index];
}
