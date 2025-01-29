# import string
# from os import getenv
# from datetime import datetime

# import pytest
# from httpx import ASGITransport, AsyncClient
# from dotenv import load_dotenv

# from backend.main import app


# load_dotenv()
# API_URL = getenv("API_URL")


# @pytest.mark.asyncio
# async def test_create_team():
#     async with AsyncClient(transport=ASGITransport(app=app), base_url=API_URL) as ac:
#         data = {
#             "name": "Zmiiny Testovy",
#             "region": "UA",
#             "game": "raid shadow legends",
#             "foundation_date": datetime.now(),
#             "players": [],
#             "coach": "Andrei B1ad3 Gorodenskiy",
#             # "achievements": [],
#             "social_media": [],
#             "logo": bytes(1),
#             "active": True,
#         }
#         response = await ac.post("/team/create", data=data)

#         assert response.status_code == 200

# DEPRECATED !!!
# TODO Tests for new teams model
