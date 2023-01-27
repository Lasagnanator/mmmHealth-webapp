from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


'''form per login entrambi utenti'''
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

'''
Form per Registrazione del dottore
'''
class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    phoneNumber = StringField('Phone Number', validators=[DataRequired()])  #sotto forma di stringa così non è modificabile
    submit = SubmitField('Register')

#TODO:creare altri form per filtrare risultati qua sotto