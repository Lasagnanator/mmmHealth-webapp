from datetime import datetime
from app import db


# Vedere come impostare le foreing key
# da integrare in my_site
class Login_patient(db.Model):
    __tablename__ = 'login_patient'
    patient_id    = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(64), index=True, unique=True)
    password      = db.Column(db.String(128))

    def __repr__(self) -> str:
        return "<Login_patient(patient_id='{}', username='{}', password_hash='{}')>"\
               .format(self.patient_id, self.username, self.password)


class Login_doctor(db.Model):
    __tablename__ = 'login_doctor'
    doctor_id     = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(64), index=True, unique=True)
    password      = db.Column(db.String(128))

    def __repr__(self) -> str:
        return "<Login_doctor(doctor_id='{}', username='{}', password_hash='{}')>"\
               .format(self.doctor_id, self.username, self.password)

# da integrare in my_site
'''
class login_patient(db.Model):
    patient_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<login_patient {}>'.format(self.username) #cosa fa?

class login_doctor(db.Model):
    doctor_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<login_doctor {}>'.format(self.username) #cosa fa?

class patient(db.Model):
    patient_id = db.Column(db.Integer, db.ForeignKey('login_patient.id'))
    email = db.Column(db.String(64))
    name = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    birthdate = db.Column(db.Date)
    gender = db.Column(db.String(64))
    height = db.Column(db.Integer)
    last_access = db.Column(db.Date)
    last_visit = db.Column(db.Date)
    last_report = db.Column(db.Date, db.ForeignKey('Report.id'))
    doctor_id = db.Column(db.String(64), db.ForeignKey('Doctor.id'))

    def __repr__(self):
        return '<patient {}>'.format(self.patient_id) #cosa fa?

class doctor(db.Model):
    doctor_id = db.Column(db.Integer, db.ForeignKey('login_doctor.id'))
    name = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    phone_number = db.Column(db.String(64))

    def __repr__(self):
        return '<doctor {}>'.format(self.doctor_id) #cosa fa?

class patient(db.Model):
    patient_id = db.Column(db.Integer, db.ForeignKey('login_patient.id'))
    fellings = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    notes = db.Column(db.String(200))
    minpressure = db.Column(db.Integer)
    maxpressure = db.Column(db.Integer)
    ecg = db.Column() # di cosa?
    spo2 = db.Column() # di cosa?
    date = db.Column(db.Date)
    
    last_report = db.Column(db.Date, db.ForeignKey('Report.id'))
    
    def __repr__(self):
        return '<patient {}>'.format(self.patient_id) #cosa fa?
'''