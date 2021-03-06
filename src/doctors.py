from flask import Blueprint, request
from src.medicsdb import Doctors

doctors_blueprint = Blueprint('doctors', __name__)


@doctors_blueprint.route('/doctors/', methods=['GET'])
def doctors():
    if request.method == "GET":
        selected_doctors = Doctors.query.all()
        collected_data = doctors_data(selected_doctors)
        return {
            "doctors": collected_data
        }

def doctors_data(data):
    doctors = []
    for each in data:
        doctors.append({
            "doc_id":each.doc_id,
            "name":each.name,
            "email":each.email,
            "phone":each.phone,
            "specialization":each.specialization
        })
    return {"succes":"true", "doctors": doctors, "msg": "doctors details loaded successfully"}