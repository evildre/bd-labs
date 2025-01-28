from datetime import date
from sqlalchemy import create_engine, desc, func, sql
from sqlalchemy.orm import sessionmaker, class_mapper
from main import clinic, selection_clinic, doctor, doctor_schedule, patient, visit  
from add import adding

engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/lab_5_db")
session_class = sessionmaker(bind=engine)
session = session_class()

adding()

def row_to_dict(row):
    result = {}
    for column in row._fields:
        value = getattr(row, column)
        if isinstance(value, (list, dict, tuple)):
            value = row_to_dict(value)
        result[column] = value
    return result


def proceed_query_1(request_arguments):
    selected_patient_surname = request_arguments.get("patient_surname")

    if selected_patient_surname is None:
        return "Undefined"

    query_text = """
        SELECT patient.address, visit.visit_date, visit.diagnosis
        FROM patient
        JOIN visit on visit.patient_id = patient.patient_id
        WHERE patient.surname = :selected_patient_surname
        LIMIT 1;
    """
    results = session.execute(sql.text(query_text), {"selected_patient_surname": selected_patient_surname})
    result_dicts = [row_to_dict(row) for row in results]


    return result_dicts


def proceed_query_2(request_arguments):
    selected_patient_surname = request_arguments.get("patient_surname")

    if selected_patient_surname is None:
        return "Undefined"

    query_2 = session.query(func.concat(doctor.surname, ' ', func.substring(doctor.name, 1, 1), '.', ' ',
                                    func.substring(doctor.patronymic, 1, 1), '.').label("doctor_name"),
                            visit.diagnosis.label("diagnosis"),
                            visit.visit_date + visit.term.label("end_date")) \
        .join(visit, doctor.doctor_id == visit.doctor_id) \
        .join(patient, visit.patient_id == patient.patient_id) \
        .filter(patient.surname == selected_patient_surname)
    results = query_2.all()
    result_dicts = [row_to_dict(row) for row in results]

    return result_dicts

def proceed_query_3(request_arguments):
    selected_doctor_surname = request_arguments.get("doctor_surname")

    if selected_doctor_surname is None:
        return "Undefined"

    query_text = """
        SELECT DISTINCT doctor_schedule.cabinet, doctor_schedule.reception_date
        FROM doctor
        JOIN doctor_schedule on doctor_schedule.doctor_id = doctor.doctor_id
        WHERE doctor.surname = :selected_doctor_surname
    """
    results = session.execute(sql.text(query_text), {"selected_doctor_surname": selected_doctor_surname})
    result_dicts = [row_to_dict(row) for row in results]

    return result_dicts
    

def proceed_query_4(request_arguments):
    selected_doctor_surname = request_arguments.get("doctor_surname")

    if selected_doctor_surname is None:
        return "Undefined"

    query_4 = session.query(patient.surname, patient.name, patient.patronymic,
                            visit.visit_date, visit.diagnosis, visit.appointments, visit.complaints) \
        .join(visit, patient.patient_id == visit.patient_id) \
        .join(doctor, visit.doctor_id == doctor.doctor_id) \
        .filter(doctor.surname == selected_doctor_surname, (visit.visit_date + visit.term) >= date(2023, 10, 25))
    results = query_4.all()
    result_dicts = [row_to_dict(row) for row in results]

    return result_dicts

def proceed_query_5(request_arguments):
    selected_diagnosis = request_arguments.get("diagnosis")

    if selected_diagnosis is None:
        return "Undefined"

    try:
        results = session.execute(sql.text(f"SELECT appointments FROM visit WHERE diagnosis = '{selected_diagnosis}'"))
        ret = [row_to_dict(row) for row in results]
        return ret
    except Exception as e:
        print(f"Error: {e}")
        return "Internal error"
    

def proceed_query_6(request_arguments):
    selected_area = request_arguments.get("area")
    selected_cab = request_arguments.get("cab")

    if selected_area is None:
        return "Undefined"
    
    if selected_cab is None:
            return "Undefined"
    

    query_6 = session.query(doctor.surname, doctor.name, doctor.patronymic, doctor_schedule.cabinet) \
        .join(doctor_schedule, doctor.doctor_id == doctor_schedule.doctor_id) \
        .filter(doctor_schedule.reception_date == date(2023, 10, 23),
                doctor_schedule.name_area == selected_area,
                doctor_schedule.cabinet == selected_cab)
    results= query_6.all()
    result_dicts = [row_to_dict(row) for row in results]
    return result_dicts


def proceed_query_7(request_arguments):
    query_7 = session.query(doctor.surname, doctor.name, doctor.patronymic,
                            func.count(visit.visit_id).label("numPatients")) \
        .join(doctor_schedule, doctor.doctor_id == doctor_schedule.doctor_id) \
        .join(visit, doctor_schedule.schedule_id == visit.doctor_id) \
        .filter(visit.visit_date >= date(2023, 10, 1), visit.visit_date <= date(2023, 10, 31)) \
        .group_by(doctor.surname, doctor.name, doctor.patronymic) \
        .order_by(desc("numPatients"))
    results = query_7.all()
    result_dicts = [row_to_dict(row) for row in results]
    return result_dicts

def proceed_query_8(request_arguments):
    selected_patient_surname = request_arguments.get("patient_surname")

    if selected_patient_surname is None:
        return "Undefined"

    results = session.execute(sql.text(f"SELECT patient.address FROM patient WHERE patient.surname = '{selected_patient_surname}'"))
    print(results)
    result_dicts = [row_to_dict(row) for row in results]

    return result_dicts



queries_list = [proceed_query_1, proceed_query_2, proceed_query_3, proceed_query_4, proceed_query_5, proceed_query_6, proceed_query_7, proceed_query_8]
