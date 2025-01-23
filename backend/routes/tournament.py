from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select

from ..db import Tournament, AsyncDB
from ..schemas import TournamentModel


tournament_router = APIRouter(prefix="/tournament", tags=["Tournament"])


@tournament_router.post("/create_new_tournament", status_code=status.HTTP_201_CREATED, summary="Create Tournament")
async def create_tournament(data: TournamentModel,
                            session=Depends(AsyncDB.get_session)
                        ):
        check_tournament_exists = await session.scalar(
            select(Tournament).where(Tournament.name == data.name)
        )
        if check_tournament_exists:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Tournament with name `{data.name}` already exists"
            )
        tournament = Tournament(**data.model_dump())
        session.add(tournament)
        return {"message": "Tournament created successfully"}


