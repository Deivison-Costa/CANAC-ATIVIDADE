"use client";

import type React from "react";
import { useState } from "react";
import { Search, Loader2, MapPin } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card } from "@/components/ui/card";
import { WeatherDisplay } from "@/components/weather-display";
import { toast } from "sonner";
import type { WeatherData } from "@/lib/types";

export function WeatherSearch() {
  const [city, setCity] = useState("");
  const [weatherData, setWeatherData] = useState<WeatherData | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!city.trim()) {
      toast.error("Location Required", {
        description: "Please enter a city name to get weather data",
      });
      return;
    }

    setIsLoading(true);

    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";
      const response = await fetch(
        `${apiUrl}/api/v1/weather?city=${encodeURIComponent(city)}`,
      );

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || "Failed to fetch weather data");
      }

      const data = await response.json();
      setWeatherData(data);
    } catch (error) {
      toast.error("Error Fetching Data", {
        description:
          error instanceof Error
            ? error.message
            : "Unable to retrieve weather information",
      });
      setWeatherData(null);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="max-w-5xl mx-auto space-y-8">
      <Card className="p-6 md:p-8 shadow-lg border-2">
        <form onSubmit={handleSearch} className="space-y-4">
          <div className="flex flex-col sm:flex-row gap-3">
            <div className="flex-1 relative">
              <MapPin className="absolute left-4 top-1/2 -translate-y-1/2 h-5 w-5 text-muted-foreground" />
              <Input
                type="text"
                placeholder="Enter city name (e.g., São Paulo, Ribeirão Preto, London)"
                value={city}
                onChange={(e) => setCity(e.target.value)}
                disabled={isLoading}
                className="w-full pl-12 h-12 text-base"
              />
            </div>
            <Button
              type="submit"
              disabled={isLoading}
              size="lg"
              className="h-12 px-8 font-semibold"
            >
              {isLoading ? (
                <>
                  <Loader2 className="mr-2 h-5 w-5 animate-spin" />
                  Searching
                </>
              ) : (
                <>
                  <Search className="mr-2 h-5 w-5" />
                  Get Weather
                </>
              )}
            </Button>
          </div>
          <p className="text-sm text-muted-foreground text-center">
            Search for any city worldwide to view current weather conditions and
            forecasts
          </p>
        </form>
      </Card>

      {weatherData && <WeatherDisplay data={weatherData} />}
    </div>
  );
}
