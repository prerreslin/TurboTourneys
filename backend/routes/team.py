from typing import Annotated

from fastapi import APIRouter, Depends, Form, status

from ..schemas import TeamScheme
from ..db import AsyncDB, Team


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
