from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from wtforms_alchemy import PhoneNumberField
from datetime import date, datetime




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
    phoneNumber = PhoneNumberField('Phone Number', validators=[DataRequired()], region='IT') #campo numero di telefono
    password    = PasswordField('Password', validators=[DataRequired()])
    password_c  = PasswordField('Conferma Password', validators=[DataRequired(),EqualTo('password', message='le password devono combaciare')]) #controllo per validazione
    submit      = SubmitField('Register')




#TODO:creare altri form per filtrare risultati qua sotto

'''
filtra i pazienti del medico 
possible_names è temporaneo e va sostituito con la lista di tutti i pazienti del DB
TODO: il validator della data non funziona
'''
possible_names = {0:'Giovanni Genovesi',
            1:'Giorgio De Davide',
            3:'Pier Paolo Paulari',
            4:'Paolo Pier DePieri',
            5:'Luca Nervi',
            6:'MariaGiuseppa Paolina', 
            7:'Paolina Giuseppini'} 

'''
def validate_date(form, field):
    if datetime(field.data).date() > date.today():
        raise ValidationError("stai cercando Marty McFly?")
    #elif form.field.data < date.(year=1900, month=1, day=1):
    #   raise ValidationError("davvero cerchi un vecchio con una app? dai dai") 
    print('errore data')
    return ValidationError
'''
class PatientFilters(FlaskForm):

    date        = DateField  ('data ultimo report', format='%d-%m-%Y') 
    dateOrder   = SelectField('ordina report per data', choices=[(True, 'dal più recente'), (False,'dal meno recente')]) #se true ordine decrescente, se false crescente
    alfabetico  = SelectField('ordine alfabetico', choices=[(True, 'A-Z'), (False,'Z-A')]) #se true ordine decrescente, se false crescente
    byName      = SelectField("inserisci il nome", choices=[(name) for name in possible_names.items()])
    submit      = SubmitField('Cerca')

def validate_on_submit(self):
            result = super(PatientFilters, self).validate()
            if (self.date.data>date.today):
                raise ValidationError("stai cercando Marty McFly?")
                print ('errore nella data')
            else:
                print ('data ok')
                return result


    
    
      
