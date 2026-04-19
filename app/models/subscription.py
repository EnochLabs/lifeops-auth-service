from datetime import datetime, timezone
from typing import Optional

from beanie import Document
from pydantic import Field


class Subscription(Document):
    user_id: str
    plan: str
    status: str
    period_start: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    period_end: datetime
    grace_end: Optional[datetime] = None

    class Settings:
        name = "subscriptions"
