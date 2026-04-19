from datetime import datetime, timezone
from typing import Optional

from beanie import Document
from pydantic import EmailStr, Field


class User(Document):
    email: EmailStr
    username: str
    hashed_password: str
    is_active: bool = True
    role: str = "USER"
    current_plan: str = "FREE"

    class Settings:
        name = "users"
