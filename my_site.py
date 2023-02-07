from app import app, db, query
from app.models import Login_patient, Login_doctor, Patient, Doctor, Report


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'login_patient': Login_patient,
        'login_doctor': Login_doctor,
        'patient': Patient,
        'doctor': Doctor,
        'report': Report,
        'q': query,
        }