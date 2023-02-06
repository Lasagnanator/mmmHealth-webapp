from app import db
from app.models import Login_doctor, Doctor, Report, Patient
from app.utils import hash512

#controlla se la password inserita coincide con quella inserita nel DB con quell'username
def passwdcheck(password, username):
    result = db.session.execute(db.select(Login_doctor.password).where(Login_doctor.username == username )).first()
    if result[0] == hash512(password):
        check = True
    else :
        check = False  
    return check

#restituisce l'id del medico che fa il login
def id_doctor(username):
    result = db.session.execute(db.select(Login_doctor.doctor_id).where(Login_doctor.username == username )).first()
    return result[0]

#recupera tutti i dati del medico dato un id
#da rivedere appena le tables sono pronte
def select_all(doctor_id):
    result = db.session.execute(db.select(Doctor).where(Doctor.doctor_id == doctor_id )).first()
    return result[0]

#recupera la lista degli id dei pazienti dato un id di un medico
def doc_patients(doctor_id):
    result = db.session.execute(db.select(Patient.patient_id).where(Login_doctor.doctor_id == Patient.doctor_id )).all() 
    #TODO: teest per vedere come tirare fuoir i dati come voglio io
    for patient in result:
        print (result[patient])
    return result[0]
    
######### ########## ########quey per filtrare i pazienti ######### ######### #########

#pazienti in ordine alfabetico
def patient_filters(doctor_id, alfabetico): 
    result
    if alfabetico:
        result= db.session.execute(db.select(Patient.patient_id).where(Doctor.doctor_id == doctor_id).orderBy(Doctor.name)).all()
    else:
        result= db.session.execute(db.select(Patient.patient_id).where(Doctor.doctor_id == doctor_id).orderBy(Doctor.name)).all()#inveritre ordine alfabetico, come?
    return result

#solo paziente selezionato
def patient_filters(doctor_id, byName): 
    result =   db.session.execute(db.select(Patient.patient_id).where(Doctor.doctor_id == doctor_id, Patient.name == byName)).first()
    return result

#solo i report di data byDate e ordinati per alfabetico
#TODO: inseririe inner join con tabella report per ordinarli per data
'''
def patient_filters(doctor_id, byDate, alfabetico):
    result
    if alfabetico:
        result= db.session.execute(db.select(Patient.patient_id).where(Doctor.doctor_id == doctor_id,)  .orderBy(Patient.name))
    else:
        result= db.session.execute(db.select(Patient.patient_id).where(Doctor.doctor_id == doctor_id).  orderBy(Patient.name))#inveritre ordine alfabetico, come?
    return result
    '''