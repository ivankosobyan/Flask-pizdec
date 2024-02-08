from models import Doctors, Services
from db import db
from app import app


#from datetime import datetime

with app.app_context():
    db.drop_all()
    db.create_all()


with app.app_context():
    doctors = Doctors(name ="Аронндит",surname = "Дарксайдов",specialization="Зубной (фей)")
    db.session.add(doctors)
    doctors = Doctors(name="Изольдия", surname = "Вениаминовна", specialization="Уролог")
    db.session.add(doctors)
    doctors = Doctors(name ="Кирилл", surname = "Въюгов",specialization="ЛОР")
    db.session.add(doctors)
    db.session.commit()
