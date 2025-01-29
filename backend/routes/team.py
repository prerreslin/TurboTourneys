from os import getenv
from typing import Annotated, List, Optional
from datetime import datetime, date

from fastapi import APIRouter, Depends, Form, Query, status, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from dotenv import load_dotenv

from ..schemas import TeamScheme
from ..utils import get_current_user
from ..db import AsyncDB, Team, User, TeamRating, Game


team_router = APIRouter(prefix="/team", tags=["Team"])
load_dotenv()
STATIC_URL = getenv("STATIC_URL")


@team_router.post(
    "/create_team", status_code=status.HTTP_201_CREATED, summary="Creating The Team"
)
async def create_team(
    data: Annotated[TeamScheme, Form(media_type="multipart/form-data")],
    current_user: Annotated[User, Depends(get_current_user)],
    session: Annotated[
        AsyncSession,
        Depends(AsyncDB.get_session),
    ],
):

    data_dict = data.model_dump()
    team = Team(**data_dict)
    team.roster.append(current_user)
    session.add(team)
    return "Team Created"


@team_router.post("/test_create", summary="Test Root")
async def test_create(session=Depends(AsyncDB.get_session)):

    user = await session.scalar(select(User).where(User.email == "user@example.com"))
    team = Team(
        name="TestName",
        region="TestRegion",
        founded_year=datetime.now(),
        roster=[user],
        social_media="TestSocialMedia",
        logo_path="backend/mock/images/кріса_ink.jpg",
        active=True,
    )
    session.add(team)

    test_game = await session.scalar(
        select(Game).where(Game.name == "Raid Shadow Legends")
    )
    team_testgame_rating = TeamRating(elo=100, team=team, game=test_game)
    session.add(team_testgame_rating)

    return {"message": "done"}


@team_router.get("/my_team", summary="Get Your Team")
async def my_team(
    current_user: Annotated[User, Depends(get_current_user)],
    session=Depends(AsyncDB.get_session),
):
    team = await session.scalar(select(Team).where(Team.id == current_user.team_id))

    if team:
        return team
    return {"message": "No team found"}


@team_router.get(
    "/team/{team_name}", response_model=TeamScheme, summary="Get Team Info"
)
async def team_info(team_name: str, session=Depends(AsyncDB.get_session)):
    team = await session.scalar(select(Team).where(Team.name == team_name))
    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Team with name {team_name} not found",
        )
    return team


@team_router.get("/all_teams", response_model=List[TeamScheme], summary="Get All Teams")
async def get_all_teams(session=Depends(AsyncDB.get_session)):
    all_teams = await session.scalars(select(Team))
    all_teams = [TeamScheme.model_validate(team.__dict__) for team in all_teams]

    return all_teams


@team_router.get("/filter", response_model=List[TeamScheme], summary="Filtering Teams")
async def filter_team(
    name: Optional[str] = Query(None, description="Filter by team name"),
    region: Optional[str] = Query(None, description="Filter by team region"),
    active: Optional[bool] = Query(None, description="Filter by active status"),
    founded_year: Optional[date] = Query(None, description="Filter by founding year"),
    session=Depends(AsyncDB.get_session),
):
    query = select(Team)

    if name:
        query = query.where(Team.name.ilike(f"%{name}%"))
    if region:
        query = query.where(Team.region.ilike(f"%{region}%"))
    if active is not None:
        query = query.where(Team.active == active)
    if founded_year:
        query = query.where(Team.founded_year == founded_year)

    results = await session.scalars(query)

    if not results:
        raise HTTPException(
            status_code=404, detail="No teams found with the provided filters"
        )
    return results.all()

    # @team_router.get("/leave_team")
    # async def leave_team(
    #     current_user: Annotated[User, Depends(get_current_user)],
    #     session=Depends(AsyncDB.get_session),
    # ):
    #     current_user = await session.scalar(select(User).where)

    if current_user.team:
        current_user.team.roster.remove(current_user)
        current_user.team_id = None
        current_user.team = None

        await session.commit()

        return {"message": "You have left the team"}

    return {"message": "You are not in team now"}
