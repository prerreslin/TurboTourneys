from httpx import ASGITransport, AsyncClient
from flask import Flask, render_template, request, redirect, flash, url_for


from .. import flask_app, app, API_URL
from ..forms import RegisterForm, LoginForm


@flask_app.get("/register")
def register():
    form = RegisterForm()
    return render_template("auth_form.html", form=form)


@flask_app.post("/register")
async def register_post():
    form = RegisterForm()
    if form.validate_on_submit():
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url=API_URL
        ) as ac:
            data = {
                "email": form.email.data,
                "name": form.name.data,
                "password": form.password.data,
            }

        response = await ac.post("/user/register", json=data)
        if response.status_code == 202:
            return redirect(url_for("login"))

    return render_template("auth_form.html", form=form)


@flask_app.get("/login")
def login():
    form = LoginForm()
    return render_template("auth_form.html", form=form)


@flask_app.post("/login")
async def register_post():
    form = RegisterForm()
    if form.validate_on_submit():
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url=API_URL
        ) as ac:
            data = {
                "username": form.name.data,
                "password": form.password.data,
            }

        response = await ac.post("/user/login", data=data)
        if response.status_code == 202:
            return redirect(url_for("index"))

    return render_template("auth_form.html", form=form)
