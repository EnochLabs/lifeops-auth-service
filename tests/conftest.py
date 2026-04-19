from contextlib import asynccontextmanager
from typing import Generator

import pytest
from beanie import init_beanie
from fastapi.testclient import TestClient
from mongomock_motor import AsyncMongoMockClient

from app.main import create_app
from app.models.audit_log import AuditLog
from app.models.refresh_token import RefreshToken
from app.models.subscription import Subscription
from app.models.user import User

# We'll use a mock database for tests
TEST_DATABASE_NAME = "lifeops_auth_test"


@asynccontextmanager
async def mock_lifespan(app):
    yield


@pytest.fixture(autouse=True)
async def init_test_db():
    client = AsyncMongoMockClient()
    models = [User, Subscription, RefreshToken, AuditLog]

    await init_beanie(
        database=client[TEST_DATABASE_NAME],
        document_models=models,
    )
    yield


@pytest.fixture
def client() -> Generator:
    # Create app and replace lifespan with mock
    app = create_app()
    app.router.lifespan_context = mock_lifespan
    with TestClient(app) as c:
        yield c
