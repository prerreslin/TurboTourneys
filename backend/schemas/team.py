from typing import Annotated, List, Optional
from datetime import date, datetime

from fastapi import File, UploadFile, Form
from pydantic import BaseModel, Field, field_validator

from .user import UserEmail


class TeamScheme(BaseModel):
    name: str
    region: str
    founded_year: date
    roster: Annotated[List[UserEmail], Form()]
    social_media: Optional[List[str]]
    logo: Annotated[UploadFile, File(...)] = None
    active: bool

    @field_validator("name")
    @classmethod
    def check_name(cls, value: str):
        if len(value) < 2:
            raise ValueError("The team name cannot be less than 2 letters long")
        return value
