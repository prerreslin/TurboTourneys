import asyncio

from uvicorn import run as run_asgi

from backend.main import app
from backend.db import AsyncDB


async def migrate():
    await AsyncDB.migrate()

if __name__ == "__main__":
    asyncio.run(migrate())
    run_asgi(app)
