from datetime import datetime
from app import db


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#     posts = db.relationship('Post', backref='author', lazy='dynamic')

#     def __repr__(self):
#         return '<User {}>'.format(self.username)


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __repr__(self):
#         return '<Post {}>'.format(self.body)

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
