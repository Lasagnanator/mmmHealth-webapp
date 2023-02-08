from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField, EmailField, IntegerField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Length
from wtforms_alchemy import PhoneNumberField
from datetime import date
from app import query as q
from flask import session


hash =  input 
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
    
    name        = StringField('Nome', validators=[DataRequired(), Length(min=1, max=50)])
    lastname    = StringField('Cognome', validators=[DataRequired(),Length(min=1, max=50)])
    username    = StringField('Username', validators=[DataRequired(), Length(min=1, max=15)])
    phoneNumber = PhoneNumberField('Numero di telefono', validators=[DataRequired()], region='IT') 
    password    = PasswordField('Password', validators=[DataRequired(),Length(min=5, max=64)])
    password_c  = PasswordField('Conferma Password', validators=[DataRequired(),EqualTo('password', message='le password devono combaciare')]) 
    submit      = SubmitField('Registrati')

class RegistrationPzForm(FlaskForm):
    
    name        = StringField('Nome', validators=[DataRequired(), Length(min=1, max=255)])
    lastname    = StringField('Cognome', validators=[DataRequired(), Length(min=1, max=255)])
    username    = StringField('Username', validators=[DataRequired(), Length(min=1, max=15)])
    sex         = SelectField('Genere', choices=[('Maschio', 'Maschio'), ('Femmina','Femmina')])  #scelta restituisce un boolean 
    birthdate   = DateField  ('Data di nascita', validators=[DataRequired()])
    height      = IntegerField('Altezza', validators=[DataRequired()])
    email       = EmailField ('Email', validators=[DataRequired()]) 
    submit      = SubmitField('Registrati')


'''
filtra i pazienti del medico 
possible_names è temporaneo e va sostituito con la lista di tutti i pazienti del DB
TODO: il validator della data non funziona
'''
class PatientFilters(FlaskForm):

    byDate      = DateField('data report')
    dateOrder   = SelectField('ordina report per data', choices=[(True, 'dal più recente'), (False,'dal meno recente')]) #se true ordine decrescente, se false crescente
    alfabetico  = SelectField('ordine alfabetico', choices=[(True, 'A-Z'), (False,'Z-A')]) #se true ordine decrescente, se false crescente
    # byName      = SelectField("inserisci il nome", choices=[(name) for name in possible_names.items()])
    byName      = SelectField("inserisci il nome", validate_choice=False)
    submit      = SubmitField("Cerca")


def validate_on_submit(self):
            result = super(PatientFilters, self).validate()
            if (self.date.data>date.today):
                raise ValidationError("stai cercando Marty McFly?")
                print ('errore nella data')
            else:
                print ('data ok')
                return result


#campo note libere del medico 
#da implementare
class DoctorReport(FlaskForm):
     freeField   = StringField ('campo libero', validators=[Length(min=0,max=3000)])
     submit      = SubmitField('Salva')

    
    
      
