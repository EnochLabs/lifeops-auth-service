from redis.asyncio import Redis, from_url
import fakeredis.aioredis
from app.config.settings import settings

def get_redis_client():
    if settings.ENVIRONMENT == "test":
        return fakeredis.aioredis.FakeRedis()
    return from_url(settings.REDIS_URL, decode_responses=True)

redis_client: Redis = get_redis_client()
