from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


class Base(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)


class AsyncDB:
    ENGINE = create_async_engine("sqlite+aiosqlite:///database.db")
    SESSION = sessionmaker(bind=ENGINE, class_=AsyncSession)

    @classmethod
    async def up(cls):
        async with cls.ENGINE.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @classmethod
    async def down(cls):
        async with cls.ENGINE.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    @classmethod
    async def migrate(cls):
        async with cls.ENGINE.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @classmethod
    async def get_session(cls):
        async with cls.SESSION.begin() as session:
            yield session

    @classmethod
    async def create_roles(cls):
        async with cls.SESSION.begin() as session:
            player_role = Role(name="Player")
            coach_role = Role(name="Coach")
            session.add(player_role, coach_role)

    @classmethod
    async def create_games(cls):
        async with cls.SESSION.begin() as session:
            raid_sh = Game(name="Raid Shadow Legends", description="TEst")
            session.add(raid_sh)


from .models import User, Team, Role, Game, TeamRating, Tournament
