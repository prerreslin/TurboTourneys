from typing import List
from datetime import date

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Base


class Team(Base):
    __tablename__ = "teams"

    name: Mapped[str]
    region: Mapped[str]
    founded_year: Mapped[date]
    players: Mapped[List["User"]] = relationship(back_populates="team")
    coach: Mapped["User"] = relationship(back_populates="team_coaching")
    # rating:
    social_media: Mapped[List[str]] = mapped_column(nullable=True)
    logo: Mapped[bytes]
    active: Mapped[bool]
