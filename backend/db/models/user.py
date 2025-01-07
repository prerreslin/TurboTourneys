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
    team: Mapped["Team"] = relationship(back_populates="roster")

    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), default=1)
    role: Mapped["Role"] = relationship(back_populates="users")
