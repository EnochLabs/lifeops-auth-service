from datetime import datetime
from typing import Optional

from beanie import Document


class Subscription(Document):
    user_id: str
    plan: str
    status: str
    period_start: datetime
    period_end: datetime
    grace_end: Optional[datetime] = None

    class Settings:
        name = "subscriptions"
