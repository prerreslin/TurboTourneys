from httpx import ASGITransport, AsyncClient
from flask import Flask, render_template, request, redirect, flash, url_for

from .. import flask_app, app, API_URL
from ..forms import RegisterForm, LoginForm, TeamCreateForm, TournamentCreate

@flask_app.get("/team_create")
def create_team():
    form = TournamentCreate()
    return render_template("team_create.html", form=form)

@flask_app.post("/team_create")
async def create_team_post():
    form = TournamentCreate()
    if form.validate_on_submit():
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url=API_URL
        ) as ac:
            data = {
                "name": form.name.data,
                "description": form.description.data,
                "winnings": form.winnings.data,
                "join_cost": form.join_cost.data,
            }

        response = await ac.post("/tournament/create_tournament", data=data)
        if response.status_code == 202:
            return redirect("/")

    return render_template("team_create.html", form=form)