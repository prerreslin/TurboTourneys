import pytest
from httpx import ASGITransport, AsyncClient

from backend.main import app


# ЩОБ ЗАПУСТИТИ ВВЕСТИ: pytest в термінал


@pytest.mark.anyio
async def test_login():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000"
    ) as ac:
        response = await ac.post("/auth/login")

    assert response.status_code == 200


@pytest.mark.anyio
async def test_register():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000"
    ) as ac:
        response = await ac.post("/auth/register")

    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_user():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://127.0.0.1:8000"
    ) as ac:
        test_email = "test@gmail.com"
        response = await ac.get(f"/auth/get_user/{test_email}")

    assert response.status_code == 200
