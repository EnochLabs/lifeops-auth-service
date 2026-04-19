from beanie import Document
from datetime import datetime, timezone
from typing import Optional

class Subscription(Document):
    user_id: str
    plan: str
    status: str
    period_start: datetime
    period_end: datetime
    grace_end: Optional[datetime] = None

    class Settings:
        name = "subscriptions"
