from datetime import datetime
from typing import Any, Dict, Optional

from beanie import Document


class AuditLog(Document):
    user_id: Optional[str] = None
    action: str
    metadata: Dict[str, Any]
    timestamp: datetime = datetime.utcnow()

    class Settings:
        name = "audit_logs"
