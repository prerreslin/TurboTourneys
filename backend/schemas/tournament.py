from typing import Optional

from pydantic import BaseModel, Field, field_validator


class TournamentModel(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, description="Name of the tournament")
    description: str = Field(..., min_length=10, max_length=500, description="Description of the tournament")
    winnings: str = Field(..., min_length=3, max_length=100, description="Tournament award")
    join_cost: Optional[int] = Field(None, ge=0, description="Cost to join the tournament")


    @field_validator("join_cost")
    @classmethod
    def check_join_cost(cls, value):
        if value <= 0:
            raise ValueError("The cost must be higher then 0")
        return value