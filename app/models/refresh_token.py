from beanie import Document
from datetime import datetime, timezone

class RefreshToken(Document):
    user_id: str
    token_hash: str
    expires_at: datetime
    created_at: datetime = datetime.now(timezone.utc)

    class Settings:
        name = "refresh_tokens"
