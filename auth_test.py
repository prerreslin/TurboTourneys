import string
from os import getenv
import random
from datetime import datetime

import pytest
from httpx import ASGITransport, AsyncClient
from dotenv import load_dotenv

from backend.main import app


# ЩОБ ЗАПУСТИТИ ВВЕСТИ: pytest в термінал
load_dotenv()
API_URL = getenv("API_URL")
random_email = "".join(random.choice(string.ascii_letters) for _ in range(10)).lower()


@pytest.mark.asyncio
async def test_register():
    print(API_URL)
    async with AsyncClient(transport=ASGITransport(app=app), base_url=API_URL) as ac:

        data = {
            "email": f"{random_email}@gmail.com",
            "name": f"test{random_email}",
            "password": "Test12345678_",
        }
        response = await ac.post("/user/register", json=data)
        print(response.json())

    assert response.status_code == 201


@pytest.mark.asyncio
async def test_login():
    async with AsyncClient(transport=ASGITransport(app=app), base_url=API_URL) as ac:
        data = {
            "username": f"test{random_email}",
            "password": "Test12345678_",
        }
        response = await ac.post("/user/login", data=data)
        print(response.json())

    assert response.status_code == 200
    assert type(response.json().get("access_token")) == str
    assert response.json().get("token_type") == "bearer"


@pytest.mark.asyncio
async def test_get_user():
    async with AsyncClient(transport=ASGITransport(app=app), base_url=API_URL) as ac:
        test_email = f"{random_email}@gmail.com"
        response = await ac.get(f"/user/get_user/{test_email}")
        print(response.json())

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_team():
    async with AsyncClient(transport=ASGITransport(app=app), base_url=API_URL) as ac:
        data = {
            "name": "Zmiiny Testovy",
            "region": "UA",
            "game": "raid shadow legends",
            "foundation_date": datetime.now(),
            "players": [],
            "coach": "Andrei B1ad3 Gorodenskiy",
            # "achievements": [],
            "social_media": [],
            "logo": bytes(1),
            "active": True,
        }
        response = await ac.post("/team/create", data=data)

        assert response.status_code == 200
