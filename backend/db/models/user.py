from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from .. import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int]
    email: Mapped[str]
    name: Mapped[str]
    password: Mapped[str]

    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=True)
    team: Mapped["Team"] = relationship("Team", back_populates="players", foreign_keys="[User.team_id]")

    team_coaching_id: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=True)
    team_coaching: Mapped["Team"] = relationship("Team", back_populates="coach", foreign_keys="[User.team_coaching_id]")