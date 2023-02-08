from flask import render_template, flash, redirect, url_for, session
from flask_login import LoginManager, login_user, current_user, UserMixin, login_required
from app import app
import app.forms as f
import app.query as q
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
        check = q.passwdcheck(form.password.data, form.username.data )
        if check:
            doctor_id = q.id_doctor(form.username.data)
            session['doctor_id'] = doctor_id
            login_user(q.id_doctor(form.username.data), remember=form.remember_me.data)
            return redirect(url_for('index'))
        else: 
            return render_template('login.html',  title='Sign In', form=form, error = 'password sbagliata')
    return render_template('login.html',  title='Sign In', form=form, error= '')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = f.RegistrationForm()
    if form.validate_on_submit():
        flash('registration requested for user {}'.format(
            form.name.data))
        print(form.name.data, form.lastname.data, form.password.data ) 
        return redirect(url_for('login'))
    return render_template('registration.html', title='Registration', form=form) 


@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    doctor_id = session.get('doctor_id', None)
    doctor_data = q.select_all_doctor(doctor_id)
    patient_list = q.doc_patients(doctor_id)
    names_list = q.doctor_patients(doctor_id, True)
    form = f.PatientFilters()
    form.byName.choices = names_list
    #if form.validate_on_submit():
        
       # flash ('filter patiets by {}'.format(form.alfabetico.data))  #aggiungere order by name alla query
    return render_template('index.html', title='profilo doc', 
                           form         = form,
                           doctor_data  = doctor_data,
                           patient_list = patient_list)
    
       
@app.route('/registrazionePz', methods=['GET', 'POST'])
@login_required
def registrazionePz():
    doctor_id = session.get('doctor_id', None)
    form = f.RegistrationPzForm()
    if form.validate_on_submit():
        pw_autogen = ''.join(random.choice(string.ascii_lowercase) for i in range(8))#da inviare a DB
        print(pw_autogen)
        return redirect(url_for('index'))
    return render_template('registrazionePz.html', title= 'Registrazione nuovo paziente', form= form)


'''
recupero della variabile patient_id da index
'''
@app.route('/<patient_id>/homePz', methods=['GET', 'POST'])
@login_required
def homePz(patient_id):
    #TODO: aggiungere dati del doc in alto a dx
    doctor_id  = session.get('doctor_id', None) 
    session['patient_id'] = patient_id
    #visualizzazione tutti dati del paziente selezionato
    patient_data = q.select_all_patient(patient_id)
    report_list  = q.reports(patient_id) 
    
    return render_template('homePz.html',title='home di '+ patient_data.lastname+' '+patient_data.name, patient_data = patient_data, report_list = report_list)


@app.route('/<report_id>/reportPz', methods=['GET', 'POST'])
@login_required
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
