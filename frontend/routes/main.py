from httpx import ASGITransport, AsyncClient
from flask import Flask, render_template, request, redirect, flash, url_for

from .. import flask_app, app, API_URL
from ..forms import RegisterForm, LoginForm


@flask_app.get("/")
async def index():

    return render_template("index.html")



@flask_app.get("/search")
async def search():
    query = request.args.get('query','')
    if query:
        return render_template("index.html", query = query)