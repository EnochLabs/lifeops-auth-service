from mongomock_motor import AsyncMongoMockClient
from motor.motor_asyncio import AsyncIOMotorClient

from app.config.settings import settings


def get_client():
    if settings.ENVIRONMENT == "test":
        return AsyncMongoMockClient()
    return AsyncIOMotorClient(settings.MONGODB_URL)


client = get_client()
db = client[settings.DATABASE_NAME]
