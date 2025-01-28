from main import clinic, selection_clinic, doctor, doctor_schedule, patient, visit  
from datetime import date
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, class_mapper
def adding():

    engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/lab_5_db")
    Session = sessionmaker(bind=engine)
    session = Session()
    
    clinics = [
        clinic(title='Пироговка'),
        clinic(title='Сеченовка'),
        clinic(title='Поповка'),
    ]
    session.add_all(clinics)
    session.commit()



    selection_clinics = [
        selection_clinic(name_area='Северный округ', title='Поповка'),
        selection_clinic(name_area='Южный округ', title='Поповка'),
        selection_clinic(name_area='Дзержинский район', title='Пироговка'),
        selection_clinic(name_area='Промышленный район', title='Пироговка'),
        selection_clinic(name_area='Центральный район', title='Сеченовка'),
        selection_clinic(name_area='Ленинский район', title='Сеченовка'),
    ]
    session.add_all(selection_clinics)
    session.commit()

    doctors = [
        doctor(doctor_id = 1, surname='Киндий', name='Михаил', patronymic='Иванович', category='Психиатор', birth_date=date(2001, 3, 16)),
        doctor(doctor_id = 2, surname='Старков', name='Иван', patronymic='Андреевич', category='Дерматолог', birth_date=date(2001, 2, 24)),
        doctor(doctor_id = 3, surname='Крылов', name='Андрей', patronymic='Владиславович', category='Хирург', birth_date=date(1999, 6, 3)),
        doctor(doctor_id = 4, surname='Артамонов', name='Владислав', patronymic='Даниилович', category='Гастроэнтеролог', birth_date=date(1999, 9, 3)),
        doctor(doctor_id = 5, surname='Шурубцов', name='Даниил', patronymic='Егорович', category='Психиатор', birth_date=date(2004, 1, 13)),
        doctor(doctor_id = 6, surname='Угнивенко', name='Егор', patronymic='Кириллович', category='Инфекционист', birth_date=date(2002, 10, 16)),
        doctor(doctor_id = 7, surname='Кузнецов', name='Кирилл', patronymic='Сергеевич', category='Крендеолог', birth_date=date(2002, 8, 27)),
        doctor(doctor_id = 8, surname='Зеленцов', name='Сергей', patronymic='Романович', category='Дерматолог', birth_date=date(1995, 9, 17)),
        doctor(doctor_id = 9, surname='Соцков', name='Роман', patronymic='Никитич', category='Гомолог', birth_date=date(1999, 12, 3)),
        doctor(doctor_id = 10, surname='Зюзюков', name='Никита', patronymic='Артурович', category='Стоматолог', birth_date=date(2003, 6, 11)),
        doctor(doctor_id = 11, surname='Мусаев', name='Артур', patronymic='Михайлович', category='Педиатр', birth_date=date(2003, 6, 13)),
        doctor(doctor_id = 12, surname='Ширяев', name='Егор', patronymic='Артурович', category='Инфекционист', birth_date=date(2001, 5, 6)),
    ]
    session.add_all(doctors)
    session.commit()


    doctor_schedules = [
        doctor_schedule(schedule_id=1, reception_date=date(2023, 10, 23), name_area='Северный округ', cabinet=101, doctor_id=1),
        doctor_schedule(schedule_id=2, reception_date=date(2023, 10, 23), name_area='Южный округ', cabinet=102, doctor_id=2),
        doctor_schedule(schedule_id=3, reception_date=date(2023, 10, 23), name_area='Дзержинский район', cabinet=103, doctor_id=3),
        doctor_schedule(schedule_id=4, reception_date=date(2023, 10, 23), name_area='Промышленный район', cabinet=104, doctor_id=4),
        doctor_schedule(schedule_id=5, reception_date=date(2023, 10, 23), name_area='Центральный район', cabinet=105, doctor_id=5),
        doctor_schedule(schedule_id=6, reception_date=date(2023, 10, 24), name_area='Северный округ', cabinet=106, doctor_id=6),
        doctor_schedule(schedule_id=7, reception_date=date(2023, 10, 24), name_area='Южный округ', cabinet=107, doctor_id=7),
        doctor_schedule(schedule_id=8, reception_date=date(2023, 10, 24), name_area='Дзержинский район', cabinet=108, doctor_id=8),
        doctor_schedule(schedule_id=9, reception_date=date(2023, 10, 24), name_area='Промышленный район', cabinet=109, doctor_id=9),
        doctor_schedule(schedule_id=10, reception_date=date(2023, 10, 24), name_area='Центральный район', cabinet=110, doctor_id=10),
        doctor_schedule(schedule_id=11, reception_date=date(2023, 10, 25), name_area='Северный округ', cabinet=111, doctor_id=11),
        doctor_schedule(schedule_id=12, reception_date=date(2023, 10, 25), name_area='Южный округ', cabinet=112, doctor_id=1),
        doctor_schedule(schedule_id=13, reception_date=date(2023, 10, 25), name_area='Дзержинский район', cabinet=113, doctor_id=2),
        doctor_schedule(schedule_id=14, reception_date=date(2023, 10, 25), name_area='Промышленный район', cabinet=114, doctor_id=3),
        doctor_schedule(schedule_id=15, reception_date=date(2023, 10, 25), name_area='Центральный район', cabinet=115, doctor_id=4),
        doctor_schedule(schedule_id=16, reception_date=date(2023, 10, 26), name_area='Северный округ', cabinet=116, doctor_id=5),
        doctor_schedule(schedule_id=17, reception_date=date(2023, 10, 26), name_area='Южный округ', cabinet=117, doctor_id=6),
        doctor_schedule(schedule_id=18, reception_date=date(2023, 10, 26), name_area='Дзержинский район', cabinet=118, doctor_id=7),
        doctor_schedule(schedule_id=19, reception_date=date(2023, 10, 26), name_area='Промышленный район', cabinet=119, doctor_id=8),
        doctor_schedule(schedule_id=20, reception_date=date(2023, 10, 26), name_area='Центральный район', cabinet=120, doctor_id=9),
        doctor_schedule(schedule_id=21, reception_date=date(2023, 10, 27), name_area='Северный округ', cabinet=121, doctor_id=10),
        doctor_schedule(schedule_id=22, reception_date=date(2023, 10, 27), name_area='Южный округ', cabinet=122, doctor_id=11),
        doctor_schedule(schedule_id=23, reception_date=date(2023, 10, 27), name_area='Дзержинский район', cabinet=123, doctor_id=1),
        doctor_schedule(schedule_id=24, reception_date=date(2023, 10, 27), name_area='Промышленный район', cabinet=124, doctor_id=2),
        doctor_schedule(schedule_id=25, reception_date=date(2023, 10, 27), name_area='Центральный район', cabinet=125, doctor_id=3),
    ]
    session.add_all(doctor_schedules)
    session.commit()

    patients = [
        patient(patient_id=1, surname='Поршнев', name='Роман', patronymic='Дмитриевич', address='Фрунзенская 10', sex='М', age=20),
        patient(patient_id=2, surname='Кривоченко', name='Дмитрий', patronymic='Михайлович', address='Покерная 217', sex='М', age=20),
        patient(patient_id=3, surname='Новицкий', name='Михаил', patronymic='Даниилович', address='Лесная 532', sex='М', age=20),
        patient(patient_id=4, surname='Павлов', name='Даниил', patronymic='Романович', address='Беговая 420', sex='М', age=20),
        patient(patient_id=5, surname='Басыров', name='Владимир', patronymic='Егорович', address='Петербургская 1', sex='М', age=20),
        patient(patient_id=6, surname='Лобанов', name='Егор', patronymic='Александрович', address='Королева 239', sex='М', age=20),
        patient(patient_id=7, surname='Маркуш', name='Александр', patronymic='Артурович', address='Белорусская 1', sex='М', age=20),
        patient(patient_id=8, surname='Мусаев', name='Артур', patronymic='Романович', address='Творожок 15', sex='М', age=20),
    ]
    session.add_all(patients)
    session.commit()

    visits = [
        visit(visit_id=1, visit_date=date(2023, 10, 15), diagnosis='Грипп', appointments='Прописаны антибиотики и отдых',
            complaints='Температура, кашель', given_leave=True, term=7, patient_id=1, doctor_id=2),
        visit(visit_id=2, visit_date=date(2023, 10, 15), diagnosis='Аллергия', appointments='Назначены антигистаминные препараты',
            complaints='Сыпь, зуд', given_leave=False, term=0, patient_id=2, doctor_id=3),
        visit(visit_id=3, visit_date=date(2023, 10, 16), diagnosis='Пневмония', appointments='Назначены антибиотики и режим',
            complaints='Высокая температура, боль в груди', given_leave=True, term=10, patient_id=3, doctor_id=4),
        visit(visit_id=4, visit_date=date(2023, 10, 16), diagnosis='Травма руки', appointments='Наложен гипс',
            complaints='Упал, болят рука и запястье', given_leave=True, term=14, patient_id=4, doctor_id=5),
        visit(visit_id=5, visit_date=date(2023, 10, 17), diagnosis='Гастрит', appointments='Диета и противовоспалительные препараты',
            complaints='Боль в желудке, изжога', given_leave=False, term=0, patient_id=5, doctor_id=6),
        visit(visit_id=6, visit_date=date(2023, 10, 17), diagnosis='Мигрень', appointments='Назначены анальгетики и покой',
            complaints='Сильная головная боль, тошнота', given_leave=True, term=5, patient_id=6, doctor_id=7),
        visit(visit_id=7, visit_date=date(2023, 10, 18), diagnosis='Операция по удалению аппендикса', appointments='Экстренная операция',
            complaints='Сильная боль в правом боку', given_leave=True, term=1, patient_id=7, doctor_id=8),
        visit(visit_id=8, visit_date=date(2023, 10, 18), diagnosis='Зубная боль', appointments='Назначено лечение и анестезия',
            complaints='Пульсирующая боль в зубе', given_leave=True, term=3, patient_id=8, doctor_id=9),
        visit(visit_id=9, visit_date=date(2023, 10, 19), diagnosis='Грипп', appointments='Прописаны антибиотики и отдых',
            complaints='Температура, кашель', given_leave=True, term=7, patient_id=7, doctor_id=10),
        visit(visit_id=10, visit_date=date(2023, 10, 19), diagnosis='Аллергия', appointments='Назначены антигистаминные препараты',
            complaints='Сыпь, зуд', given_leave=False, term=0, patient_id=5, doctor_id=11),
        visit(visit_id=11, visit_date=date(2023, 10, 20), diagnosis='Пневмония', appointments='Назначены антибиотики и режим',
            complaints='Высокая температура, боль в груди', given_leave=True, term=10, patient_id=1, doctor_id=2),
        visit(visit_id=12, visit_date=date(2023, 10, 20), diagnosis='Травма руки', appointments='Наложен гипс',
            complaints='Упал, болят рука и запястье', given_leave=True, term=14, patient_id=2, doctor_id=3),
        visit(visit_id=13, visit_date=date(2023, 10, 21), diagnosis='Гастрит', appointments='Диета и противовоспалительные препараты',
            complaints='Боль в желудке, изжога', given_leave=False, term=0, patient_id=3, doctor_id=4),
        visit(visit_id=14, visit_date=date(2023, 10, 21), diagnosis='Мигрень', appointments='Назначены анальгетики и покой',
            complaints='Сильная головная боль, тошнота', given_leave=True, term=5, patient_id=4, doctor_id=5),
        visit(visit_id=15, visit_date=date(2023, 10, 22), diagnosis='Операция по удалению аппендикса', appointments='Экстренная операция',
            complaints='Сильная боль в правом боку', given_leave=True, term=1, patient_id=5, doctor_id=6),
        visit(visit_id=16, visit_date=date(2023, 10, 22), diagnosis='Зубная боль', appointments='Назначено лечение и анестезия',
            complaints='Пульсирующая боль в зубе', given_leave=True, term=3, patient_id=6, doctor_id=7),
        visit(visit_id=17, visit_date=date(2023, 10, 23), diagnosis='Ожог', appointments='Лечение ожога и перевязка',
            complaints='Боль, покраснение кожи', given_leave=True, term=10, patient_id=7, doctor_id=8),
        visit(visit_id=18, visit_date=date(2023, 10, 23), diagnosis='Синусит', appointments='Противовоспалительные препараты и обильное питье',
            complaints='Заложенность носа, головная боль', given_leave=True, term=7, patient_id=2, doctor_id=8),
        visit(visit_id=19, visit_date=date(2023, 10, 24), diagnosis='Операция по удалению аппендикса', appointments='Экстренная операция',
            complaints='Сильная боль в правом боку', given_leave=True, term=1, patient_id=7, doctor_id=9),
        visit(visit_id=20, visit_date=date(2023, 10, 24), diagnosis='Зубная боль', appointments='Назначено лечение и анестезия',
            complaints='Пульсирующая боль в зубе', given_leave=True, term=3, patient_id=8, doctor_id=10),
        visit(visit_id=21, visit_date=date(2023, 10, 25), diagnosis='Ожог', appointments='Лечение ожога и перевязка',
            complaints='Боль, покраснение кожи', given_leave=True, term=10, patient_id=6, doctor_id=11),
        visit(visit_id=22, visit_date=date(2023, 10, 25), diagnosis='Синусит', appointments='Противовоспалительные препараты и обильное питье',
            complaints='Заложенность носа, головная боль', given_leave=True, term=7, patient_id=2, doctor_id=1),
        visit(visit_id=23, visit_date=date(2023, 10, 26), diagnosis='Операция по удалению аппендикса', appointments='Экстренная операция',
            complaints='Сильная боль в правом боку', given_leave=True, term=1, patient_id=7, doctor_id=2),
        visit(visit_id=24, visit_date=date(2023, 10, 26), diagnosis='Зубная боль', appointments='Назначено лечение и анестезия',
            complaints='Пульсирующая боль в зубе', given_leave=True, term=3, patient_id=8, doctor_id=3),
        visit(visit_id=25, visit_date=date(2023, 10, 27), diagnosis='Ожог', appointments='Лечение ожога и перевязка',
            complaints='Боль, покраснение кожи', given_leave=True, term=10, patient_id=6, doctor_id=4),
        visit(visit_id=26, visit_date=date(2023, 10, 27), diagnosis='Синусит', appointments='Противовоспалительные препараты и обильное питье',
            complaints='Заложенность носа, головная боль', given_leave=True, term=7, patient_id=2, doctor_id=5),
        visit(visit_id=27, visit_date=date(2023, 10, 28), diagnosis='Операция по удалению аппендикса', appointments='Экстренная операция',
            complaints='Сильная боль в правом боку', given_leave=True, term=1, patient_id=7, doctor_id=6),
        visit(visit_id=28, visit_date=date(2023, 10, 28), diagnosis='Зубная боль', appointments='Назначено лечение и анестезия',
            complaints='Пульсирующая боль в зубе', given_leave=True, term=3, patient_id=8, doctor_id=7),
        visit(visit_id=29, visit_date=date(2023, 10, 29), diagnosis='Ожог', appointments='Лечение ожога и перевязка',
            complaints='Боль, покраснение кожи', given_leave=True, term=10, patient_id=6, doctor_id=8),
        visit(visit_id=30, visit_date=date(2023, 10, 29), diagnosis='Синусит', appointments='Противовоспалительные препараты и обильное питье',
            complaints='Заложенность носа, головная боль', given_leave=True, term=7, patient_id=2, doctor_id=9),
        visit(visit_id=31, visit_date=date(2023, 10, 30), diagnosis='Операция по удалению аппендикса', appointments='Экстренная операция',
            complaints='Сильная боль в правом боку', given_leave=True, term=1, patient_id=7, doctor_id=10),
        visit(visit_id=32, visit_date=date(2023, 10, 30), diagnosis='Зубная боль', appointments='Назначено лечение и анестезия',
            complaints='Пульсирующая боль в зубе', given_leave=True, term=3, patient_id=8, doctor_id=11),
        visit(visit_id=33, visit_date=date(2023, 10, 31), diagnosis='Ожог', appointments='Лечение ожога и перевязка',
            complaints='Боль, покраснение кожи', given_leave=True, term=10, patient_id=6, doctor_id=1),
        visit(visit_id=34, visit_date=date(2023, 10, 31), diagnosis='Синусит', appointments='Противовоспалительные препараты и обильное питье',
            complaints='Заложенность носа, головная боль', given_leave=True, term=7, patient_id=2, doctor_id=3),
    ]

    session.add_all(visits)
    session.commit()
