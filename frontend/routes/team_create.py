from httpx import ASGITransport, AsyncClient
from flask import Flask, render_template, request, redirect, flash, url_for

from .. import flask_app, app, API_URL
from ..forms import RegisterForm, LoginForm, TeamCreateForm

@flask_app.get("/team_create")
def create_team():
    form = TeamCreateForm()
    return render_template("team_create.html", form=form)

@flask_app.post("/team_create")
async def create_team_post():
    form = TeamCreateForm()
    if form.validate_on_submit():
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url=API_URL
        ) as ac:
            data = {
                "name": form.name.data,
                "logo": form.logo.data,
                "team_members": form.team_members.data,
            }

        response = await ac.post("/team/create_team", data=data)
        if response.status_code == 202:
            return redirect("/")

    return render_template("team_create.html", form=form)