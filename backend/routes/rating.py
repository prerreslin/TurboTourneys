from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select

from ..db import AsyncDB, TeamRating, User, Team
from ..utils import get_current_user


rating_router = APIRouter(prefix="/rating", tags=["Rating"])


@rating_router.get("/all_ratings")
async def all_ratings(session=Depends(AsyncDB.get_session)):
    ratings = await session.scalars(select(TeamRating))
    ratings = ratings.all()
    return ratings


@rating_router.get("/ratings")
async def user_team_ratings(
    current_user: Annotated[User, Depends(get_current_user)],
    session=Depends(AsyncDB.get_session),
):
    # Ratings of current user`s team, need to make dynamic filters in frontend
    user_team_id = current_user.team_id

    ratings = await session.scalars(
        select(TeamRating).where(TeamRating.team_id == user_team_id)
    )

    return ratings.all()
