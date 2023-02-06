from datetime import datetime
from app import db


# Vedere come impostare le foreing key
# da integrare in my_site
class Login_patient(db.Model):
    __tablename__ = 'login_patient'
    patient_id    = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password      = db.Column(db.String(128), nullable=False)

    def __repr__(self) -> str:
        return "<Login_patient(patient_id='{}', username='{}', password_hash='{}')>"\
               .format(self.patient_id, self.username, self.password)


class Login_doctor(db.Model):
    __tablename__ = 'login_doctor'
    doctor_id     = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password      = db.Column(db.String(128), nullable=False)

    def __repr__(self) -> str:
        return "<Login_doctor(doctor_id='{}', username='{}', password_hash='{}')>"\
               .format(self.doctor_id, self.username, self.password)

class Patient(db.Model):
    patient_id = db.Column(db.Integer, db.ForeignKey('login_patient.id'), primary_key=True)
    doctor_id = db.Column(db.String(64), db.ForeignKey('login_doctor.id'), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    sex = db.Column(db.String(64), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    medical_plan = db.Column(db.String(64))
    last_access = db.Column(db.Date)
    last_visit = db.Column(db.Date)

    def __repr__(self):
        return "<Patient (name='{}', lastname='{}')>"\
               .format(self.name, self.lastname)

class Doctor(db.Model):
    doctor_id = db.Column(db.Integer, db.ForeignKey('login_doctor.id'), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    phone_number = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return "<Doctor (name='{}', lastname='{}')>"\
               .format(self.name, self.lastname)

class Report(db.Model):
    report_id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('login_patient.id'), nullable=False)
    feelings = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(200))
    sys = db.Column(db.Integer, nullable=False)
    dia = db.Column(db.Integer, nullable=False)
    bpm = db.column(db.Integer)
    spo2 = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    
    def __repr__(self):
        return "<Report (patient_id='{}', report_id='{}')>"\
               .format(self.patient_id)