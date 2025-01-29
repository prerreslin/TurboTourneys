from pydantic import BaseModel, Field, field_validator, EmailStr

from ..utils import get_password_hash


class UserModel(BaseModel):
    email: EmailStr = Field(..., description="Email of user")
    name: str = Field(..., description="Username of user")
    password: str = Field(..., min_length=8, description="Password of user")

    @field_validator("password")
    @classmethod
    def check_and_hash_password(cls, value):
        if not any(char.isupper() for char in value):
            raise ValueError("Password must contain at least one uppercase letter")

        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit")

        if not any(char in "!@#$%^&*()-_+=<>?/\\|[]{}~" for char in value):
            raise ValueError("Password must contain at least one special character")

        value = get_password_hash(value)

        return value


class UserResponse(BaseModel):
    email: str
    name: str
    password: str


class UserEmail(BaseModel):
    email: EmailStr = Field(..., description="Email of user")
