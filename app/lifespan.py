from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient

from app.config.settings import settings
from app.models.audit_log import AuditLog
from app.models.refresh_token import RefreshToken
from app.models.subscription import Subscription
from app.models.user import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize MongoDB and Beanie
    logger.info("Initializing MongoDB connection...")
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    app.state.db_client = client

    models = [User, Subscription, RefreshToken, AuditLog]

    await init_beanie(database=client[settings.DATABASE_NAME], document_models=models)
    logger.info("Beanie initialized with models.")

    yield

    # Shutdown: Close MongoDB connection
    logger.info("Closing MongoDB connection...")
    client.close()
    logger.info("MongoDB connection closed.")
