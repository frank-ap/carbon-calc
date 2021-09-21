from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from data_dict import stadiums

class CarbonCalculator(FlaskForm):
    teams = SelectField('teams', choices=[], validators=[DataRequired()])
    postcodes = SelectField('What is the first part of your postcode?', choices=['egg'], validators=[DataRequired()])
    vehicle = SelectField('How do you travel to your home matches?', choices=[], validators=[DataRequired()])
    games = SelectField('How many matches a season do you attend?', choices=[], validators=[DataRequired()])
    #car_type = SelectField('What type of car do you have?', choices=[], validators=[DataRequired()])
    #alerted = SelectField('Alerted every', choices=['Day', 'Week', 'Month'], validators=[DataRequired()])
    submit = SubmitField('Submit')
