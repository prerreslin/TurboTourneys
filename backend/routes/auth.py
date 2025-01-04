from typing import Annotated
from datetime import timedelta

from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status

from ..schemas import Token, UserModel, UserResponse
from ..utils import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from ..db import AsyncDB, User


users_router = APIRouter(prefix="/user", tags=["User"])


@users_router.post("/login")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[Session, Depends(AsyncDB.get_session)],
) -> Token:
    user = await authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await create_access_token(
        data={"sub": user.name}, expires_delta=access_token_expires
    )
    print(type(access_token))
    return Token(access_token=access_token, token_type="bearer")


@users_router.post(
    "/register", summary="Register Account", status_code=status.HTTP_201_CREATED
)
async def register_user(
    data: UserModel, session: Annotated[Session, Depends(AsyncDB.get_session)]
):
    user = await session.scalar(select(User).where(User.email == data.email))
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = await session.scalar(select(User).where(User.name == data.name))
    if user:
        raise HTTPException(status_code=400, detail="Nickname already registered")
    user = User(**data.model_dump())
    session.add(user)
    return user


@users_router.get(
    "/get_user/{email}", response_model=UserResponse, summary="Get User Info"
)
async def get_user(
    email: str, session: Annotated[Session, Depends(AsyncDB.get_session)]
):
    user = await session.scalar(select(User).where(User.email == email))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with email {email} not found",
        )
    return user
