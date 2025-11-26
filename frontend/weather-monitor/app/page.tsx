import { WeatherSearch } from "@/components/weather-search";
import { Cloud } from "lucide-react";

export default function Home() {
  return (
    <main className="min-h-screen bg-linear-to-br from-background via-background to-accent/20">
      <div className="container mx-auto px-4 py-12 md:py-16 lg:py-20">
        <div className="mb-12 md:mb-16 text-center max-w-3xl mx-auto">
          <div className="inline-flex items-center justify-center w-16 h-16 md:w-20 md:h-20 rounded-2xl bg-primary/10 mb-6">
            <Cloud className="w-8 h-8 md:w-10 md:h-10 text-primary" />
          </div>
          <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold text-foreground mb-4 text-balance tracking-tight">
            Weather Intelligence
          </h1>
          <p className="text-lg md:text-xl text-muted-foreground max-w-2xl mx-auto text-pretty leading-relaxed">
            Real-time meteorological data and insights for agricultural
            monitoring and sugarcane field management
          </p>
        </div>

        <WeatherSearch />
      </div>
    </main>
  );
}
