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
    logo_path: Mapped[str] = mapped_column(nullable=True)
    active: Mapped[bool]

    roster: Mapped[List["User"]] = relationship(back_populates="team")
    ratings: Mapped[List["TeamRating"]] = relationship(back_populates="team")
