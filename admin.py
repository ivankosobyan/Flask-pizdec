from flask_admin import Admin
from app import app
from flask_admin.contrib.sqla import ModelView
from db import db
from models import Doctors,Services

admin = Admin(app, "Admin panel",template_mode="bootstrap3")

class DoctorsModelView(ModelView):
    column_labels=dict(name="Имя",surname="Фамилия",specialization='Профессия',created_at="Создано в:",updated_at="Обновленов в:")
    column_editable_list=["name","surname","specialization"]
    form_excluded_columns=["created_at","updated_at"]

class ServicesModelView(ModelView):
    column_labels=dict(prise="Цена",title="Название",tipe="Тип услуги")
    column_editable_list=["prise"]
    form_excluded_columns=["created_at","updated_at","title","tipe"]

admin.add_view(DoctorsModelView(Doctors,db.session))
admin.add_view(ServicesModelView(Services,db.session))