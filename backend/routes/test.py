from typing import Annotated

from fastapi import APIRouter, Depends

from ..utils import get_current_user

test_router = APIRouter(prefix="/test", tags=['Test'])


@test_router.get("/")
async def test_root(current_user: Annotated[str, Depends(get_current_user)]):
    return f'User {current_user.email}'