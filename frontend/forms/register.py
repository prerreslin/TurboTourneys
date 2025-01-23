from flask_wtf import FlaskForm
from wtforms import (
    EmailField,
    StringField,
    PasswordField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Email,
)


class RegisterForm(FlaskForm):
    email = EmailField( "Enter your Email Address:",
        validators=[
            DataRequired(),
            Email(),
        ]
    )

    name = StringField("Enter your name:",
        validators=[DataRequired()]
    )

    password = PasswordField("Enter your password:",
        validators=[
            DataRequired(),
        ]
    )
    password_confirm = PasswordField("Re-enter your pasword:", validators=[DataRequired(), EqualTo("password")])

    submit = SubmitField("Register")
