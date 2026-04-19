from typing import Optional
from beanie import Document
from datetime import datetime, timezone
from typing import Any, Dict

class AuditLog(Document):
    user_id: Optional[str] = None
    action: str
    metadata: Dict[str, Any]
    timestamp: datetime = datetime.now(timezone.utc)

    class Settings:
        name = "audit_logs"
