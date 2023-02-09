from flask import render_template, flash, redirect, url_for, session
from app import app
from app import db
from app.utils import hash512
import app.forms as f
import app.query as q
import app.models as m
import random, string

@app.route('/')
def root():
    return redirect(url_for('landing'))
@app.route('/landing')
def landing():
    return render_template('landing.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = f.LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))

        try: 
            check = q.passwdcheck(form.password.data, form.username.data )
            if check:
                doctor_id = q.id_doctor(form.username.data)
                session['doctor_id'] = doctor_id
                return redirect(url_for('index'))
            else: 
                return render_template('login.html',  title='Sign In', form=form, error = 'password sbagliata')
        except:
            return render_template('login.html',  title='Sign In', form=form, error = 'nome utente non esite')

    return render_template('login.html',  title='Sign In', form=form, error= '')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = f.RegistrationForm()
    if form.validate_on_submit():
        flash('registration requested for user {}'.format(
            form.name.data))
        q.new_doctor(form)
        return redirect(url_for('login'))
    return render_template('registration.html', title='Registration', form=form) 


@app.route('/index', methods=['GET', 'POST'])
def index():
    doctor_id = session.get('doctor_id', None)
    doctor_data=q.select_all_doctor(doctor_id)
    form = f.PatientFilters()
    patient_list= q.doc_patients(doctor_id) 
    print('nome scelto', form.byName.data)
    return render_template('index.html', title='profilo doc', 
                           form         = form,
                           doctor_data  = doctor_data,
                           patient_list = patient_list)
    
       
@app.route('/registrazionePz', methods=['GET', 'POST'])
def registrazionePz():
    doctor_id = session.get('doctor_id', None)
    form = f.RegistrationPzForm()
    print(type(form.birthdate.data))
    if form.is_submitted():
        print('nel submit')
        pw_autgen = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
        q.new_patient(form, doctor_id, pw_autgen)
        message = 'nuovo paziente creato'
        print(message)
        return redirect(url_for('index'))
    return render_template('registrazionePz.html', title= 'Registrazione nuovo paziente', form= form)


'''
recupero della variabile patient_id da index
'''
@app.route('/<patient_id>/homePz', methods=['GET', 'POST'])
def homePz(patient_id):
    doctor_id  = session.get('doctor_id', None) 
    session['patient_id'] = patient_id
    patient_data = q.select_all_patient(patient_id)
    report_list  = q.reports(patient_id) 
    
    return render_template('homePz.html',title='home di '+ patient_data.lastname+' '+patient_data.name, patient_data = patient_data, report_list = report_list)


@app.route('/<report_id>/reportPz', methods=['GET', 'POST'])
def reportPz(report_id):
    patient_id  = session.get('patient_id', None)

    report_data = q.report_data(report_id)  
    patient_data= q.select_all_patient(patient_id)

    form = f.DoctorReport()
    conferma= ""
    if form.validate_on_submit():
        print(form.freeField.data)
        conferma = "documento inviato"
        print(conferma)
        return conferma
    print(form.freeField.data)

    return render_template('reportPZ.html',title='report di '+ patient_data.lastname+' '+patient_data.name, 
                           conferma     = conferma, 
                           form         = form, 
                           report_data  = report_data,
                           patient_data = patient_data)

@app.route('/presentazione')
def presentazione():
    return render_template('presentazione.html')



#-----------------error handlers--------------------
@app.errorhandler(404)
# Intercetta l'errore page not found e lancia la nostra pagina 404
def page_not_found(error):
    return render_template('404.html', title='404'), 404


@app.errorhandler(500)
# Intercetta l'errore internal server error lancia la nostra pagina 500
def internal_server_error(error):
    return render_template('500.html', title='500'), 500

#---------------------------------------------------
