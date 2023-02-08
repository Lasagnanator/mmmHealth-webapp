from app import db
from app.models import Login_doctor, Doctor, Report, Patient
from app.utils import hash512

#controlla se la password inserita coincide con quella inserita nel DB con quell'username
def passwdcheck(password: str, username: str) -> bool:
    result = db.session.execute(db.select(Login_doctor.password).where(Login_doctor.username == username )).first()
    if result[0] == hash512(password):
        check = True
    else :
        check = False  
    return check

#restituisce l'id del medico che fa il login
def id_doctor(username):
    result = db.session.execute(db.select(Login_doctor.doctor_id).where(Login_doctor.username == username)).first()
    return result[0]

#recupera tutti i dati del medico dato un id
def select_all_doctor(doctor_id):
    result = db.session.execute(db.select(Doctor).where(Doctor.doctor_id == doctor_id)).first()
    return result[0]

#recupera la lista degli id dei pazienti dato un id di un medico
def doc_patients(doctor_id):
    result = db.session.execute(db.select(Patient).where(Patient.doctor_id  == doctor_id)).all() 
    return result

#recupera tutti i dati del paziente dato un id
def select_all_patient(patient_id):
    result = db.session.execute(db.select(Patient).where(Patient.patient_id == patient_id)).first()
    return result[0]

#recupera tutti i report dato l'id di un paziente
def reports(patient_id):
    result =  db.session.execute(db.select(Report).where(Report.patient_id == patient_id)).all()
    return result

#recupera i dati di un report dato un id
def report_data(report_id):
    result =  db.session.execute(db.select(Report).where(Report.report_id == report_id)).first()
    return result[0]


######### ########## ########quey per filtrare i pazienti ######### ######### #########

#pazienti in ordine alfabetico
def doctor_patients(doctor_id: int, alfabetico: bool): 
    if alfabetico:
        result = db.session.execute(db.select(Patient.patient_id, Patient.name, Patient.lastname).where(Patient.doctor_id == doctor_id).order_by(Patient.name, Patient.lastname)).all()
    else:
        result = db.session.execute(db.select(Patient.patient_id, Patient.name, Patient.lastname).where(Patient.doctor_id == doctor_id).order_by(Patient.name.desc(), Patient.lastname.desc())).all()
    return result

def patients_list(doctor_id: int, alfabetico: bool): 
    if alfabetico:
        result = db.session.execute(db.select(Patient.patient_id, Patient.name, Patient.lastname).where(Patient.doctor_id == doctor_id).order_by(Patient.name, Patient.lastname)).all()
    else:
        result = db.session.execute(db.select(Patient.patient_id, Patient.name, Patient.lastname).where(Patient.doctor_id == doctor_id).order_by(Patient.name.desc(), Patient.lastname.desc())).all()
    name_list = []
    for row in result:
        name_list.append(row[1] + " " + row[2])
    return name_list

#solo paziente selezionato
def patient_filter(doctor_id, byName: str): 
    result =   db.session.execute(db.select(Patient.patient_id).where(Patient.doctor_id == doctor_id, Patient.name == byName)).first()
    return result


""" def get_report (doctor_id):
    query = db.select(
                Report.patient_id,  # 0
                Patient.name,       # 1
                Patient.lastname,   # 2
                Report.date,        # 3
                Report.feelings,    # 4
                Report.weight,      # 5
                Report.sys,         # 6
                Report.dia,         # 7
                Report.bpm,         # 8
                Report.spo2,        # 9
                Report.notes        # 10
                )\
                .where(Patient.doctor_id == doctor_id)\
                .join(Report, Report.patient_id == Patient.patient_id)\
                .order_by(Report.date.desc())
    result = db.session.execute(query).all()
    reports = []
    for row in result:
        entry_found = False
        for entry in reports:
            if (entry[0] == row[0]):
                entry_found = True
                break
        if (entry_found == False):
            reports.append(row)
    return reports """
                

def get_report (doctor_id):
    query = db.select(
                Report.patient_id,  # 0
                Patient.name,       # 1
                Patient.lastname,   # 2
                Report.date,        # 3
                Report.feelings,    # 4
                Report.weight,      # 5
                Report.sys,         # 6
                Report.dia,         # 7
                Report.bpm,         # 8
                Report.spo2,        # 9
                Report.notes        # 10
                ).distinct(Report.patient_id)\
                .where(Patient.doctor_id == doctor_id)\
                .join(Report, Report.patient_id == Patient.patient_id)\
                .order_by(Report.patient_id, Report.report_id.desc())
    result = db.session.execute(query).all()
    return result
        
#TODO: creare query per altre funzioni filtro