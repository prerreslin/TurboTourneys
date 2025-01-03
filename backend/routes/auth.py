from fastapi import APIRouter


auth_router = APIRouter(prefix="/auth")


@auth_router.post("/login", status_code=200)
async def login_test():
    return 200
