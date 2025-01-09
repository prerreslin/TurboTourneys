from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from .. import Base


class User(Base):
    __tablename__ = "users"

    email: Mapped[str]
    name: Mapped[str]
    password: Mapped[str]

    team_id: Mapped[UUID] = mapped_column(ForeignKey("teams.id"), nullable=True)
    team: Mapped["Team"] = relationship(back_populates="roster")

    role_id: Mapped[UUID] = mapped_column(ForeignKey("roles.id"))
    role: Mapped["Role"] = relationship(back_populates="users")
