from flask import render_template, flash, redirect, url_for, session
from app import app
import app.forms as f
import app.query as q
import random
import string


#TODO: eliminare quando riusciamo ad importare lista pazienti
patients = {'Giovanni Genovesi',
            'Giorgio De Davide',
            'Pier Paolo Paulari',
            'Paolo Pier DePieri',
            'Luca Nervi',
            'MariaGiuseppa Paolina', 
            'Paolina Giuseppini'} 

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
def index():
    doctor_id = session.get('doctor_id', None)
    doctor_data=q.select_all(doctor_id)
    #inviare la lista di pazienti con dati di base
    form = f.PatientFilters()
    if form.validate_on_submit():
        patient_list= q.doc_patients(doctor_id)
       # flash ('filter patiets by {}'.format(form.alfabetico.data))  #aggiungere order by name alla query
    print (form.byName.data)
    return render_template('index.html', title='profilo doc', 
                           patients = patients, #sostituire patient con dati DB
                           form = form,
                           doctor_data = doctor_data)
    
       
@app.route('/registrazionePz', methods=['GET', 'POST'])
def registrazionePz():
    doctor_id = session.get('doctor_id', None)
    form = f.RegistrationPzForm()
    if form.validate_on_submit():
        pw_autogen = ''.join(random.choice(string.ascii_lowercase) for i in range(8))#da inviare a DB
        print(pw_autogen)
        return redirect(url_for('index'))
    return render_template('registrazionePz.html', title= 'Registrazione nuovo paziente', form= form)



@app.route('/homePz', methods=['GET', 'POST'])
def homePz():
    doctor_id = session.get('doctor_id', None)
    #visualizzazione tutti dati del paziente selezionato
    return render_template('homePz.html',title='home di -nome pazinte-', patients= patients)#sostituire patient con dati DB


@app.route('/reportPZ', methods=['GET', 'POST'])
def reportPz():
    doctor_id = session.get('doctor_id', None)
    form = f.DoctorReport()
    conferma= ""
    if form.validate_on_submit():
        print(form.freeField.data)
        conferma = "documento inviato"
        print(conferma)
        return conferma
    print(form.freeField.data)

    return render_template('reportPZ.html',title='report di -nome pazinte-', conferma = conferma, form = form)





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
