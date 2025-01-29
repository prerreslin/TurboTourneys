from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Base


class Role(Base):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(unique=True)
    users: Mapped[List["User"]] = relationship(back_populates="role")
