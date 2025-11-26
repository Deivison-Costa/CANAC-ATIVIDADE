# Weather Monitor Frontend

Next.js-based frontend for the weather monitoring application.

## Features

- Server-side rendering with Next.js App Router
- Responsive design with Tailwind CSS
- Real-time weather data display
- Loading and error states
- Type-safe with TypeScript
- Modern UI with shadcn/ui components

## Installation

```bash
npm install
```

## Running

```bash
npm run dev
```

Visit http://localhost:3000

## Environment Variables

Create a `.env.local` file:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Build

```bash
npm run build
npm start
```

## Architecture

```
frontend/weather-monitor
├── app/
│   ├── page.tsx           # Main page
│   ├── layout.tsx         # Root layout
│   └── globals.css        # Global styles
├── components/
│   ├── weather-search.tsx # Search component
│   └── weather-display.tsx # Display component
└── lib/
    ├── types.ts           # TypeScript interfaces
    └── weather-codes.ts   # Weather code utils
```

## Technologies

- Next.js 16 with App Router
- React 19
- TypeScript
- Tailwind CSS v4
- shadcn/ui components
- Lucide icons
