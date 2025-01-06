from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Base


class User(Base):
    __tablename__ = "users"

    email: Mapped[str]
    name: Mapped[str]
    password: Mapped[str]

    team_id: Mapped[int] = mapped_column("teams.id")
    team: Mapped["Team"] = relationship(back_populates="players")

    team_coaching_id: Mapped[int] = mapped_column("teams.id")
    team_coaching: Mapped["Team"] = relationship(back_populates="coach")
