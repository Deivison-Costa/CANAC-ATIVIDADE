# Weather Monitor for Sugarcane Farming

A full-stack application that provides real-time weather information for sugarcane field monitoring. The application helps producers track weather factors such as temperature, humidity, precipitation, wind, and atmospheric pressure.

## Architecture

The application follows a clean architecture pattern with clear separation of concerns:

### Backend (FastAPI)
- **Layer Structure**:
  - `main.py`: Application entry point with FastAPI configuration
  - `app/api/routes.py`: API endpoint definitions
  - `app/services/`: Business logic layer
    - `weather_service.py`: Weather data orchestration
    - `cache_service.py`: In-memory caching implementation
  - `app/schemas/`: Pydantic models for request/response validation
  - `app/core/`: Configuration and shared utilities

- **Design Decisions**:
  - **Service Layer Pattern**: Separates business logic from API routes
  - **Repository Pattern**: Weather service acts as wrapper for external API
  - **Caching Strategy**: In-memory cache with TTL (5 minutes) to reduce API calls
  - **Async/Await**: All I/O operations use async for better performance
  - **Type Safety**: Pydantic models ensure data validation and type checking

### Frontend (Next.js)
- **Component Structure**:
  - `app/page.tsx`: Main page with search interface
  - `components/weather-search.tsx`: Search form with state management
  - `components/weather-display.tsx`: Weather data visualization
  - `lib/types.ts`: TypeScript interfaces
  - `lib/weather-codes.ts`: WMO weather code interpretation

- **Design Decisions**:
  - **Client-Side Data Fetching**: Weather data fetched on-demand for freshness
  - **Component Composition**: Separated concerns between search and display
  - **Responsive Design**: Mobile-first approach with Tailwind CSS
  - **Error Handling**: Toast notifications for user feedback
  - **Loading States**: Visual feedback during API calls

## Technology Stack

### Backend
- **FastAPI**: Modern Python web framework with automatic API documentation
- **Pydantic**: Data validation and settings management
- **httpx**: Async HTTP client for external API calls
- **Uvicorn**: ASGI server for production

### Frontend
- **Next.js 16**: React framework with App Router
- **TypeScript**: Type safety and better developer experience
- **Tailwind CSS v4**: Utility-first CSS framework
- **shadcn/ui**: High-quality React components
- **Lucide Icons**: Icon library

### External API
- **Open-Meteo**: Free weather API (no authentication required)
  - Geocoding API for city → coordinates
  - Forecast API for current weather data

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py
│   │   ├── core/
│   │   │   └── config.py
│   │   ├── schemas/
│   │   │   └── weather.py
│   │   └── services/
│   │       ├── weather_service.py
│   │       └── cache_service.py
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/weather-monitor
│   ├── app/
│   │   ├── page.tsx
│   │   ├── layout.tsx
│   │   └── globals.css
│   ├── components/
│   │   ├── weather-search.tsx
│   │   └── weather-display.tsx
│   ├── lib/
│   │   ├── types.ts
│   │   └── weather-codes.ts
│   ├── next.config.mjs
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Running the Application

### Prerequisites
- Docker and Docker Compose installed
- Ports 3000 and 8000 available

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd weather-monitor
   ```

2. **Start the application**:
   ```bash
   docker compose up
   ```

3. **Access the application**:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

4. **Stop the application**:
   ```bash
   docker compose down
   ```

### Development Mode

#### Backend Development
```bash
cd backend
poetry install
poetry shell
poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Development
```bash
cd frontend/weather-monitor
npm install
npm run dev
```

## API Endpoints

### Weather Data
```
GET /api/v1/weather?city={city_name}
```

**Query Parameters**:
- `city` (required): City name to search for

**Response Example**:
```json
{
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
  "timestamp": "2024-01-15T14:30:00"
}
```

### Health Check
```
GET /health
```

## Design Decisions

### Backend Architecture

1. **Clean Architecture**:
   - Clear separation between API routes, business logic, and data access
   - Easy to test and maintain each layer independently
   - Follows SOLID principles

2. **Caching Strategy**:
   - In-memory cache with 5-minute TTL
   - Reduces API calls to Open-Meteo
   - Improves response times for repeated queries
   - Could be easily replaced with Redis for production

3. **Error Handling**:
   - Specific exceptions for different error types
   - HTTP status codes match error semantics (404 for city not found, 500 for server errors)
   - Detailed error messages for debugging

4. **API Wrapper Pattern**:
   - Abstracts Open-Meteo API complexity
   - Two-step process: geocoding then weather fetch
   - Allows for easy API provider switching

### Frontend Architecture

1. **Component Composition**:
   - Separation of search logic and display logic
   - Reusable weather display component
   - Type-safe props with TypeScript

2. **User Experience**:
   - Immediate feedback with loading states
   - Toast notifications for errors
   - Responsive grid layout for weather metrics
   - Clear visual hierarchy

3. **Agricultural Focus**:
   - Highlighted metrics relevant to farming (temperature, humidity, precipitation, wind)
   - Color-coded data visualization
   - Weather code interpretation for easy understanding

### Docker Configuration

1. **Multi-Stage Builds**:
   - Smaller production images
   - Optimized for deployment

2. **Health Checks**:
   - Ensures backend is ready before frontend starts
   - Automatic service recovery

3. **Networking**:
   - Isolated bridge network for service communication
   - Port mapping for external access

## Weather Metrics for Sugarcane

The application highlights key weather factors that affect sugarcane development:

- **Temperature**: Optimal range 20-30°C for photosynthesis
- **Humidity**: High humidity can promote diseases
- **Precipitation**: Critical for irrigation planning
- **Wind**: Strong winds can damage crops
- **Cloud Cover**: Affects photosynthesis rates
- **Pressure**: Can indicate weather pattern changes

## Future Improvements

### Backend
- [ ] Add Redis for distributed caching
- [ ] Implement rate limiting
- [ ] Add historical weather data endpoints
- [ ] Create weather alerts based on thresholds
- [ ] Add database for storing search history
- [ ] Implement user authentication
- [ ] Add weather forecast (7-day, 14-day)
- [ ] Create batch city search endpoint

### Frontend
- [ ] Add weather graphs and charts
- [ ] Implement geolocation for automatic city detection
- [ ] Add favorite cities list
- [ ] Create weather comparison between multiple cities
- [ ] Add dark mode toggle
- [ ] Implement PWA features for offline access
- [ ] Add weather alert notifications
- [ ] Create mobile app version

### DevOps
- [ ] Add CI/CD pipeline
- [ ] Implement monitoring and logging (Prometheus, Grafana)
- [ ] Add automated tests (unit, integration, e2e)
- [ ] Set up staging environment
- [ ] Add load balancing for scalability
- [ ] Implement API rate limiting and throttling

### Features
- [ ] Soil moisture recommendations based on weather
- [ ] Pest risk assessment using weather patterns
- [ ] Harvest timing recommendations
- [ ] Irrigation scheduling suggestions
- [ ] Multi-language support (Portuguese, Spanish, English)
