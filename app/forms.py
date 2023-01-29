from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms_alchemy import PhoneNumberField



'''form per login entrambi utenti'''
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

'''
Form per Registrazione del dottoreù
crea un nuovo record su DB
TODO: un solo account per numero di telefono
'''
class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
   
    phoneNumber = PhoneNumberField('Phone Number', validators=[DataRequired()]) #campo numero di telefono
    submit = SubmitField('Register')

#TODO:creare altri form per filtrare risultati qua sotto