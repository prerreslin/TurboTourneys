from fastapi import APIRouter, FastAPI

from .routes import users_router, test_router, team_router, rating_router


app = FastAPI()

api_router = APIRouter(prefix="/api")

api_router.include_router(users_router)
api_router.include_router(test_router)
api_router.include_router(team_router)
api_router.include_router(rating_router)
app.include_router(api_router)
