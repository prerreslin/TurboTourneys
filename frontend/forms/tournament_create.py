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

from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError

def cost_validate(form, field):
    num = float(field.data)
    if num < 0:
        raise ValidationError("Cost must be no less than 0")
    
    

class TournamentCreate(FlaskForm):
    name = StringField(validators= (Length(3, 30, "Tournament name should be between 3 and 30 symbols"), DataRequired()))
    description= StringField(validators= (Length(1, 500, "Tournament name should be less than 500 characters"), DataRequired()))
    winnings = StringField(validators=DataRequired())
    join_cost = StringField(validators=cost_validate)
    submit = SubmitField("Create Tournament")