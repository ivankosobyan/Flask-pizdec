from app import app
from flask import render_template

from models import Doctors,Services

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/doctors")
def doctors():
    doctors = Doctors.query.all()
    return render_template("doctors.html", doctors=doctors)

@app.route("/analis")
def analis():    
    return render_template("analis.html")

@app.route("/zapis")
def zapis():
    services = Services.query.all()
    return render_template("zapis.html",services=services)

@app.route("/personal_doctor/<int:doctors_id>")
def personal_doctor():
    doctors = Doctors.query.all()
    return render_template("personal_doctor.html",doctors=doctors)