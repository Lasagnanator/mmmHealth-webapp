from app import app, db
from app.models import Login_patient, Login_doctor


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'login_patient': Login_patient,
        'login_doctor': Login_doctor,
        }