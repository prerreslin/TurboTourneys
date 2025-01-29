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

from datetime import datetime

from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError

def cost_validate(form, field):
    num = float(field.data)
    if num < 0:
        raise ValidationError("Cost must be no less than 0")
    
def date_validate(form, field):
    date = field.data
    date_format = '%Y/%m/%d'
    date_obj = datetime.strptime(date, date_format)
    
    if date_obj > datetime.now():
        raise ValidationError("Date cannot be in the past.")

def time_valitade(form, field):
    time = field.data
    timehs = time.split(":")
    if int(timehs[0]) > 24 or int(timehs[0]) < 0:
        raise ValidationError("Hours should be within 24")
    elif int(timehs[1]) > 59 or int(timehs[1]) < 0:
        raise ValidationError("Minutes should be within 60")

class TournamentCreate(FlaskForm):
    name = StringField("Enter the tournament name:", validators=[Length(3, 30, "Tournament name should be between 3 and 30 symbols"), DataRequired()])
    description= StringField("Enter the tournament description:",validators=[Length(1, 500, "Tournament name should be less than 500 characters"), DataRequired()])
    winnings = StringField("Enter the tournament winnings:",validators=[DataRequired()])
    join_cost = StringField("Enter the tournament join cost:",validators=[cost_validate])
    date = StringField("Enter the tournaments date(YYYY/MM/DD):",validators=[DataRequired(), date_validate])
    time = StringField("Enter the tournaments time(HH:MM)",validators=[DataRequired(), time_valitade])
    submit = SubmitField("Create Tournament")