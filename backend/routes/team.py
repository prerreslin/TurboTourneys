from typing import Annotated
from datetime import datetime

from fastapi import APIRouter, Depends, Form, status
from sqlalchemy import select

from ..schemas import TeamScheme
from ..db import AsyncDB, Team, User


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
    return {"message": "done"}
