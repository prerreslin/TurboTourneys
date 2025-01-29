from flask_wtf import FlaskForm
from wtforms import (
    EmailField,
    StringField,
    PasswordField,
    SubmitField,
    FileField,
    FieldList,
    SelectField,
    FormField
)

from fastapi import UploadFile
from PIL import Image
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError

MAX_FILE_SIZE = 1 * 1024 * 1024
img = Image

def logo_check(form, field):
    file = field.data
    if file.mimetype not in ["image/png", "image/jpeg"] and (file and len(file.read())) > MAX_FILE_SIZE:
        raise ValidationError("Image not accepted. Image must be 'png' or 'jpg', less that 1mb, and 512 by 512 px") 
    
    image = Image.open(file)
    width, height = image.size
    if width != 512 or height != 512:
        raise ValidationError("Image must be 512x512 pixels.")
    file.seek(0)


def validate_choices(self, field):
        for entry in field.entries:
            if entry.choice.data == 'Captain':
                return
        raise ValidationError("The team must have at least one 'Captain' selected.")


    
class MemberForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    role = SelectField(choices=["Captain, Member, Substitiute"], validators=[DataRequired()])


class TeamCreateForm(FlaskForm):
    team_name = StringField("Team Name:",
        validators=[
            DataRequired(),
            Length(10, 30, "Team name should be between 10 and 30 symbols"),
        ]
    )

    logo = FileField("Team Logo:",
            validators=[DataRequired(), logo_check]
    )

    team_members = FieldList("Team Members:", FormField(MemberForm), validators=[validate_choices], min_entries=3, max_entries=5)

    submit = SubmitField("Create Team")
