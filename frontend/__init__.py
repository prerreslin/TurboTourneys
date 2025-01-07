from flask import Flask
from os import getenv
from httpx import ASGITransport, AsyncClient
from dotenv import load_dotenv

from backend.main import app

load_dotenv()
API_URL = getenv("API_URL")
SECRET_KEY = getenv("SECRET_KEY")

flask_app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY


from . import routes
