from datetime import datetime, timezone

from beanie import Document
from pydantic import Field


class RefreshToken(Document):
    user_id: str
    token_hash: str
    expires_at: datetime
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    class Settings:
        name = "refresh_tokens"
