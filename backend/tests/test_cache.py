import asyncio
import pytest
from app.services.cache_service import CacheService


@pytest.mark.asyncio
async def test_cache_set_get():
    cache = CacheService()
    await cache.set("k", {"a": 1}, ttl=1)
    val = await cache.get("k")
    assert val == {"a": 1}
    await asyncio.sleep(1.1)
    val2 = await cache.get("k")
    assert val2 is None
