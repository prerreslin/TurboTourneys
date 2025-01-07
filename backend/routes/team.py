from typing import Annotated

from fastapi import APIRouter, Depends, Form, status

from ..schemas import TeamScheme
from ..db import AsyncDB, Team


team_router = APIRouter(prefix="/team", tags=['Team'])


@team_router.post("/create_team", status_code = status.HTTP_201_CREATED)
async def create_team(data: Annotated[TeamScheme, Form(media_type="multipart/form-data")],
                      session = Depends(AsyncDB.get_session)):
    # team = Team(**data_dict)
    session.add(team)
    return "Team Created"