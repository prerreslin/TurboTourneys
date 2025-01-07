from typing import List
from datetime import date

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from .. import Base


class Team(Base):
    __tablename__ = "teams"

    name: Mapped[str]
    region: Mapped[str]
    founded_year: Mapped[date]
    social_media: Mapped[str] = mapped_column(nullable=True)
    logo: Mapped[bytes]
    active: Mapped[bool]

    players: Mapped[List["User"]] = relationship("User", back_populates="team", foreign_keys="[User.team_id]")
    coach: Mapped["User"] = relationship("User", back_populates="team_coaching", foreign_keys="[User.team_coaching_id]", uselist=False)

