from typing import Optional, Any
from datetime import datetime, timedelta


class CacheService:
    """Simple in-memory cache service"""

    def __init__(self):
        self._cache: dict = {}

    def get(self, key: str) -> Optional[dict]:
        """Get value from cache if not expired"""
        if key in self._cache:
            entry = self._cache[key]
            if datetime.now() < entry["expires_at"]:
                return entry["value"]
            else:
                del self._cache[key]
        return None

    def set(self, key: str, value: Any, ttl: int):
        """Set value in cache with TTL in seconds"""
        self._cache[key] = {"value": value, "expires_at": datetime.now() + timedelta(seconds=ttl)}

    def delete(self, key: str):
        """Delete key from cache"""
        if key in self._cache:
            del self._cache[key]

    def clear(self):
        """Clear entire cache"""
        self._cache.clear()
