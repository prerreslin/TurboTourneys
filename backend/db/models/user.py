from .. import Base
from sqlalchemy.orm import Mapped


class User(Base):
        __tablename__ = "users"

        email: Mapped[str]
        name: Mapped[str]
        password: Mapped[str]
