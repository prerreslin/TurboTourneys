from typing import List, Optional
from datetime import date

from pydantic import BaseModel, Field

from .user import UserModel


class TeamScheme(BaseModel):
    name: str
    region: str
    founded_year: date
    players: List[UserModel]
    coach: Optional[UserModel]
    social_media: Optional[List[str]]
    logo: bytes
    active: bool
