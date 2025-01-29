from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Base


class Game(Base):
    __tablename__ = "games"

    name: Mapped[str]
    description: Mapped[str]

    team_ratings: Mapped[List["TeamRating"]] = relationship(
        "TeamRating", back_populates="game"
    )
