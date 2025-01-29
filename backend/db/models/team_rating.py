from datetime import date, datetime
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Base


class TeamRating(Base):
    __tablename__ = "team_ratings"

    elo: Mapped[int]
    updated_at: Mapped[date] = mapped_column(default=datetime.now())

    team_id: Mapped[UUID] = mapped_column(ForeignKey("teams.id"))
    game_id: Mapped[UUID] = mapped_column(ForeignKey("games.id"))

    team: Mapped["Team"] = relationship(back_populates="ratings")
    game: Mapped["Game"] = relationship(back_populates="team_ratings")
