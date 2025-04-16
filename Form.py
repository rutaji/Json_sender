from flask_wtf import FlaskForm
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import SubmitField, StringField
from wtforms.validators import NumberRange
from wtforms.widgets.core import NumberInput, TextArea


class JsonForm(FlaskForm):
    input = StringField("input",widget=TextArea())
    submit = SubmitField('Send')
