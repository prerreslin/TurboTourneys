from flask_wtf import FlaskForm
from wtforms import (
    EmailField,
    StringField,
    PasswordField,
    SubmitField,
    FileField,
)

from fastapi import Vali
from PIL import Image
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError

MAX_FILE_SIZE = 307200
img = Image
img.thumbnail

def logo_check(form, field):
    if (
        field.content_type not in ["image/png", "image/jpeg"]
        and field.size < MAX_FILE_SIZE and 
    ):
        raise ValidationError("Image not accepted. Image must be 'png' or 'jpg', less that 300kb, and 512 by 512 px")


class TeamCreateForm(FlaskForm):
    team_name = EmailField(
        validators=[
            DataRequired(),
            Length(10, 30, "Team name should be between 10 and 30 symbols"),
        ]
    )

    logo = FileField(
        validators=DataRequired(),
    )

    password = PasswordField(
        validators=[
            DataRequired(),
        ]
    )
    password_confirm = PasswordField(validators=[DataRequired(), EqualTo("password")])

    submit = SubmitField("Create")
