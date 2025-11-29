import asyncio
from typing import Optional, Any
from datetime import datetime, timedelta


class CacheService:
    """Simple in-memory async cache service with a lock for safety."""

    def __init__(self):
        self._cache: dict[str, dict] = {}
        self._lock = asyncio.Lock()

    async def get(self, key: str) -> Optional[Any]:
        """Get value from cache if not expired"""
        async with self._lock:
            entry = self._cache.get(key)
            if not entry:
                return None
            if datetime.now() < entry["expires_at"]:
                return entry["value"]
            del self._cache[key]
            return None

    async def set(self, key: str, value: Any, ttl: int):
        """Set value in cache with TTL in seconds"""
        async with self._lock:
            self._cache[key] = {
                "value": value,
                "expires_at": datetime.now() + timedelta(seconds=ttl),
            }

    async def delete(self, key: str):
        """Delete key from cache"""
        async with self._lock:
            if key in self._cache:
                del self._cache[key]

    async def clear(self):
        """Clear entire cache"""
        async with self._lock:
            self._cache.clear()
