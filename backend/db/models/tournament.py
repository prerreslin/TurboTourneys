from sqlalchemy.orm import Mapped

from .. import Base


class Tournament(Base):
    __tablename__ = "tournaments"
    
    name: Mapped[str]
    description: Mapped[str]
    winnings: Mapped[str]
    join_cost: Mapped[int]