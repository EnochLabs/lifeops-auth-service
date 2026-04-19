from datetime import datetime

from beanie import Document


class RefreshToken(Document):
    user_id: str
    token_hash: str
    expires_at: datetime
    created_at: datetime = datetime.utcnow()

    class Settings:
        name = "refresh_tokens"
