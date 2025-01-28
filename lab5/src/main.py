from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

base = declarative_base()

class clinic(base):
    __tablename__ = 'clinic'

    title = Column(String(255), primary_key=True, nullable=False)

class selection_clinic(base):
    __tablename__ = 'selection_clinic'

    name_area = Column(String(255), primary_key=True, nullable=False)
    title = Column(String(255), ForeignKey('clinic.title', ondelete='CASCADE'))

class doctor(base):
    __tablename__ = 'doctor'

    doctor_id = Column(Integer, primary_key=True)
    surname = Column(String(255))
    name = Column(String(255))
    patronymic = Column(String(255))
    category = Column(String(255))
    birth_date = Column(Date)

class doctor_schedule(base):
    __tablename__ = 'doctor_schedule'

    schedule_id = Column(Integer, primary_key=True)
    reception_date = Column(Date)
    name_area = Column(String(255), ForeignKey('selection_clinic.name_area', ondelete='CASCADE'))
    cabinet = Column(Integer)
    doctor_id = Column(Integer, ForeignKey('doctor.doctor_id'))

class patient(base):
    __tablename__ = 'patient'

    patient_id = Column(Integer, primary_key=True)
    surname = Column(String(255))
    name = Column(String(255))
    patronymic = Column(String(255))
    address = Column(String(255))
    sex = Column(String(2))
    age = Column(Integer)

class visit(base):
    __tablename__ = 'visit'

    visit_id = Column(Integer, primary_key=True)
    visit_date = Column(Date)
    diagnosis = Column(String(256))
    appointments = Column(String(256))
    complaints = Column(String(256))
    given_leave = Column(Boolean)
    term = Column(Integer)
    patient_id = Column(Integer, ForeignKey('patient.patient_id', ondelete='CASCADE'))
    doctor_id = Column(Integer, ForeignKey('doctor.doctor_id', ondelete='CASCADE'))

engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/lab_5_db")
base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

session.query(visit).delete()
session.query(doctor_schedule).delete()
session.query(patient).delete()
session.query(doctor).delete()
session.query(selection_clinic).delete()
session.query(clinic).delete()
session.commit()
