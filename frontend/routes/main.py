from httpx import ASGITransport, AsyncClient
from flask import Flask, render_template, request, redirect, flash, url_for

from .. import flask_app, app, API_URL
from ..forms import RegisterForm, LoginForm


@flask_app.get("/")
async def index():
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url=API_URL
        ) as ac:
        ...
    tournaments = await ac.get("/tournaments/")

    return render_template("index.html", tournaments=tournaments)

