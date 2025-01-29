from typing import Annotated, List, Optional, Set
from datetime import date, datetime

from fastapi import File, UploadFile, Form
from pydantic import BaseModel, ConfigDict, Field, field_validator, EmailStr

from .user import UserEmail


class TeamScheme(BaseModel):
    name: str
    region: str
    founded_year: date
    social_media: Optional[str]
    active: bool

    @field_validator("name")
    @classmethod
    def check_name(cls, value: str):
        if len(value) < 2:
            raise ValueError("The team name cannot be less than 2 letters long")
        return value
