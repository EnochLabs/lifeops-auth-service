from beanie import Document
from pydantic import EmailStr
from typing import Optional

class User(Document):
    email: EmailStr
    username: str
    hashed_password: str
    is_active: bool = True
    role: str = "USER"
    current_plan: str = "FREE"

    class Settings:
        name = "users"
