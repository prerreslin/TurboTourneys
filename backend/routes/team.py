from typing import Annotated
from datetime import datetime

from fastapi import APIRouter, Depends, Form, status
from sqlalchemy import select

from ..schemas import TeamScheme
from ..utils import get_current_user
from ..db import AsyncDB, Team, User, TeamRating, Game


team_router = APIRouter(prefix="/team", tags=["Team"])


@team_router.post("/create_team", status_code=status.HTTP_201_CREATED)
async def create_team(
    data: Annotated[TeamScheme, Form(media_type="multipart/form-data")],
    session=Depends(AsyncDB.get_session),
):
    logo = await data.photo.read()
    data_dict = data.model_dump()
    data_dict.pop("logo", None)
    team = Team(**data_dict, logo=logo)
    session.add(team)
    return "Team Created"


@team_router.post("/test_create")
async def test_create(session=Depends(AsyncDB.get_session)):
    with open("backend/mock/images/кріса_ink.jpg", "rb") as logo:
        logo = logo.read()

    user = await session.scalar(select(User).where(User.email == "user@example.com"))
    team = Team(
        name="TestName",
        region="TestRegion",
        founded_year=datetime.now(),
        roster=[user],
        social_media="TestSocialMedia",
        logo=logo,
        active=True,
    )
    session.add(team)

    test_game = await session.scalar(
        select(Game).where(Game.name == "Raid Shadow Legends")
    )
    team_testgame_rating = TeamRating(elo=100, team=team, game=test_game)
    session.add(team_testgame_rating)

    return {"message": "done"}


# @team_router.get("/my_team")
# async def my_team(
#     current_user: Annotated[User, Depends(get_current_user)],
#     session=Depends(AsyncDB.get_session),
# ):
#     team = await session.scalar(select(Team).where(Team.id == current_user.team_id))

#     if team:
#         return await TeamScheme.model_validate(team)
#     return {"message": "No team found"}


# @team_router.get("/leave_team")
# async def leave_team(
#     current_user: Annotated[User, Depends(get_current_user)],
#     session=Depends(AsyncDB.get_session),
# ):
#     if current_user.team:
#         current_user.team.roster.remove(current_user)
#         current_user.team_id = None
#         current_user.team = None

#     await session.commit()

#     user_team = current_user.team
#     return user_team
