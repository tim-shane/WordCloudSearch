from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    searchstring = StringField('search', validators=[DataRequired()])
    searchmodifier = StringField('searchmod')

