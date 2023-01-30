from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, ValidationError
from wtforms_alchemy import PhoneNumberField
from datetime import datetime




'''form per login entrambi utenti'''
class LoginForm(FlaskForm):
    username    = StringField('Username', validators=[DataRequired()])
    password    = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit      = SubmitField('Sign In')

'''
Form per Registrazione del dottore
crea un nuovo record su DB
TODO: un solo account per numero di telefono
'''
class RegistrationForm(FlaskForm):
    name        = StringField('Name', validators=[DataRequired()])
    lastname    = StringField('Lastname', validators=[DataRequired()])
    phoneNumber = PhoneNumberField('Phone Number', validators=[DataRequired()]) #campo numero di telefono
    submit      = SubmitField('Register')

#TODO:creare altri form per filtrare risultati qua sotto

'''
filtra i pazienti del medico 
possible_names è temporaneo e va sostituito con la lista di tutti i pazienti del DB
TODO: il validator della data non funziona
'''
possible_names={0:'Giovanni',1:'Piero',3:'Ciro',4:'Albino',5:'Paolino'} #sostituire con nomi di tutti i pazienti da DB
class PatientFilters(FlaskForm):

    def validate_date():
        if PatientFilters.date > datetime.date.today():
            raise ValidationError("stai cercando Marty McFly?")
        elif PatientFilters.date < datetime.date(year=1900, month=1, day=1):
            raise ValidationError("davvero cerchi un vecchio con una app? dai dai") 
        print('errore data')
        return ValidationError
        
    date        = DateField('data ultimo report', format='%d-%m-%Y', validators=[validate_date]) 
    dateOrder   = SelectField('ordina report per data', choices=[(True, 'dal più recente'), (False,'dal meno recente')]) #se true ordine decrescente, se false crescente
    alfabetico  = SelectField('ordine alfabetico', choices=[(True, 'A-Z'), (False,'Z-A')]) #se true ordine decrescente, se false crescente
    byName      = SelectField("inserisci il nome", choices=[(name) for name in possible_names.items()])
    submit      = SubmitField('Cerca')

        
      
