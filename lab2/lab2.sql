DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
CREATE TABLE Clinic(
	title VARCHAR(255) NOT NULL PRIMARY KEY
);

CREATE TABLE SelectionClinic(
	nameArea VARCHAR(255) NOT NULL PRIMARY KEY,
	title VARCHAR(255),
	FOREIGN KEY (title) REFERENCES Clinic(title) ON DELETE CASCADE
);

CREATE TABLE Doctor(
	doctorID SERIAL NOT NULL PRIMARY KEY,
	surname VARCHAR(255),
	name VARCHAR(255),
	patronymic VARCHAR(255),
	category VARCHAR(255),
	birthDate DATE
);

CREATE TABLE DoctorSchedule(
	scheduleID SERIAL NOT NULL PRIMARY KEY,
	receptionDate DATE,
	nameArea VARCHAR(255),
	cabinet INT,
	doctorID INT,
	FOREIGN KEY (nameArea) REFERENCES selectionClinic(nameArea) ON DELETE CASCADE
);

CREATE TABLE Patient(
	patientID SERIAL NOT NULL PRIMARY KEY,
	surname VARCHAR(255),
	name VARCHAR(255),
	patronymic VARCHAR(255),
	address VARCHAR(255),
	sex VARCHAR(2),
	age INT
);


CREATE TABLE Visit(
	visitID SERIAL NOT NULL PRIMARY KEY,
	visitDate DATE,
	diagnosis VARCHAR(256),
	appointments VARCHAR(256),
	complaints TEXT,
	givenLeave BOOLEAN,
	term INT,
	patientID INT,
	doctorID INT,
	FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON DELETE CASCADE,
	FOREIGN KEY (doctorID) REFERENCES Doctor(doctorID) ON DELETE CASCADE
);

INSERT INTO Clinic(title)
VALUES 
	('Пироговка'),
	('Сеченовка'),
	('Поповка');
	
INSERT INTO SelectionClinic(nameArea, title)
VALUES
	('Северный округ', 'Поповка'),
	('Южный округ', 'Поповка'),
	('Дзержинский район', 'Пироговка'),
	('Промышленный район', 'Пироговка'),
	('Центральный район', 'Сеченовка'),
	('Ленинский район', 'Сеченовка');
	
INSERT INTO Doctor(surname, name, patronymic, category, birthdate)
VALUES
	('Киндий', 'Михаил', 'Иванович', 'Психиатор', TO_DATE('16/03/2001', 'DD/MM/YYYY')),
	('Старков', 'Иван', 'Андреевич', 'Дерматолог', TO_DATE('24/02/2001', 'DD/MM/YYYY')),
	('Крылов', 'Андрей', 'Владиславович', 'Хирург', TO_DATE('03/06/1999', 'DD/MM/YYYY')),
	('Артамонов', 'Владислав', 'Даниилович', 'Гастроэнтеролог', TO_DATE('03/09/1999', 'DD/MM/YYYY')),
	('Шурубцов', 'Даниил', 'Егорович', 'Психиатор', TO_DATE('13/01/2004', 'DD/MM/YYYY')),
	('Угнивенко', 'Егор', 'Кириллович', 'Инфекционист', TO_DATE('16/10/2002', 'DD/MM/YYYY')),
	('Кузнецов', 'Кирилл', 'Сергеевич', 'Крендеолог', TO_DATE('27/08/2002', 'DD/MM/YYYY')),
	('Зеленцов', 'Сергей', 'Романович', 'Дерматолог', TO_DATE('17/09/1995', 'DD/MM/YYYY')),
	('Соцков', 'Роман', 'Никитич', 'Гомолог', TO_DATE('03/12/1999', 'DD/MM/YYYY')),
	('Зюзюков', 'Никита', 'Артурович', 'Стоматолог', TO_DATE('11/06/2003', 'DD/MM/YYYY')),
	('Мусаев', 'Артур', 'Михайлович', 'Педиатр', TO_DATE('13/06/2003', 'DD/MM/YYYY')),
	('Ширяев',' Егор', 'Артурович', 'Инфекционист', TO_DATE('06/05/2001', 'DD/MM/YYYY'));

INSERT INTO DoctorSchedule(receptionDate, nameArea, cabinet, doctorID)
VALUES 
    (TO_DATE('23/10/2023', 'DD/MM/YYYY'), 'Северный округ', 101, 1),
    (TO_DATE('23/10/2023', 'DD/MM/YYYY'), 'Южный округ', 102, 2),
    (TO_DATE('23/10/2023', 'DD/MM/YYYY'), 'Дзержинский район', 103, 3),
    (TO_DATE('23/10/2023', 'DD/MM/YYYY'), 'Промышленный район', 104, 4),
    (TO_DATE('23/10/2023', 'DD/MM/YYYY'), 'Центральный район', 105, 5),
    (TO_DATE('24/10/2023', 'DD/MM/YYYY'), 'Северный округ', 106, 6),
    (TO_DATE('24/10/2023', 'DD/MM/YYYY'), 'Южный округ', 107, 7),
    (TO_DATE('24/10/2023', 'DD/MM/YYYY'), 'Дзержинский район', 108, 8),
    (TO_DATE('24/10/2023', 'DD/MM/YYYY'), 'Промышленный район', 109, 9),
    (TO_DATE('24/10/2023', 'DD/MM/YYYY'), 'Центральный район', 110, 10),
    (TO_DATE('25/10/2023', 'DD/MM/YYYY'), 'Северный округ', 111, 11),
    (TO_DATE('25/10/2023', 'DD/MM/YYYY'), 'Южный округ', 112, 1),
    (TO_DATE('25/10/2023', 'DD/MM/YYYY'), 'Дзержинский район', 113, 2),
    (TO_DATE('25/10/2023', 'DD/MM/YYYY'), 'Промышленный район', 114, 3),
    (TO_DATE('25/10/2023', 'DD/MM/YYYY'), 'Центральный район', 115, 4),
    (TO_DATE('26/10/2023', 'DD/MM/YYYY'), 'Северный округ', 116, 5),
    (TO_DATE('26/10/2023', 'DD/MM/YYYY'), 'Южный округ', 117, 6),
    (TO_DATE('26/10/2023', 'DD/MM/YYYY'), 'Дзержинский район', 118, 7),
    (TO_DATE('26/10/2023', 'DD/MM/YYYY'), 'Промышленный район', 119, 8),
    (TO_DATE('26/10/2023', 'DD/MM/YYYY'), 'Центральный район', 120, 9),
    (TO_DATE('27/10/2023', 'DD/MM/YYYY'), 'Северный округ', 121, 10),
    (TO_DATE('27/10/2023', 'DD/MM/YYYY'), 'Южный округ', 122, 11),
    (TO_DATE('27/10/2023', 'DD/MM/YYYY'), 'Дзержинский район', 123, 1),
    (TO_DATE('27/10/2023', 'DD/MM/YYYY'), 'Промышленный район', 124, 2),
    (TO_DATE('27/10/2023', 'DD/MM/YYYY'), 'Центральный район', 125, 3);

INSERT INTO Patient(surname, name, patronymic, address, sex, age)
VALUES
	('Поршнев', 'Роман', 'Дмитриевич', 'Фрунзенская 10', 'М', 20),
	('Кривоченко', 'Дмитрий', 'Михайлович', 'Покерная 217', 'М', 20),
	('Новицкий', 'Михаил', 'Даниилович', 'Лесная 532', 'М', 20),
	('Павлов', 'Даниил', 'Романович', 'Беговая 420', 'М', 20),
	('Басыров', 'Владимир', 'Егорович', 'Петербургская 1', 'М', 20),
	('Лобанов', 'Егор', 'Александрович', 'Королева 239', 'М', 20),
	('Маркуш', 'Александр', 'Артурович', 'Белорусская 1', 'М', 20),
	('Мусаев', 'Артур', 'Романович', 'Творожок 15', 'М', 20);
	
INSERT INTO Visit(visitDate, diagnosis, appointments, complaints, givenLeave, term, patientID, doctorID)
VALUES 
    (TO_DATE('15/10/2023', 'DD/MM/YYYY'), 'Грипп', 'Прописаны антибиотики и отдых', 'Температура, кашель', TRUE, 7, 1, 2),
    (TO_DATE('15/10/2023', 'DD/MM/YYYY'), 'Аллергия', 'Назначены антигистаминные препараты', 'Сыпь, зуд', FALSE, 0, 2, 3),
    (TO_DATE('16/10/2023', 'DD/MM/YYYY'), 'Пневмония', 'Назначены антибиотики и режим', 'Высокая температура, боль в груди', TRUE, 10, 3, 4),
    (TO_DATE('16/10/2023', 'DD/MM/YYYY'), 'Травма руки', 'Наложен гипс', 'Упал, болят рука и запястье', TRUE, 14, 4, 5),
    (TO_DATE('17/10/2023', 'DD/MM/YYYY'), 'Гастрит', 'Диета и противовоспалительные препараты', 'Боль в желудке, изжога', FALSE, 0, 5, 6),
    (TO_DATE('17/10/2023', 'DD/MM/YYYY'), 'Мигрень', 'Назначены анальгетики и покой', 'Сильная головная боль, тошнота', TRUE, 5, 6, 7),
    (TO_DATE('18/10/2023', 'DD/MM/YYYY'), 'Операция по удалению аппендикса', 'Экстренная операция', 'Сильная боль в правом боку', TRUE, 1, 7, 8),
    (TO_DATE('18/10/2023', 'DD/MM/YYYY'), 'Зубная боль', 'Назначено лечение и анестезия', 'Пульсирующая боль в зубе', TRUE, 3, 8, 9),
    (TO_DATE('19/10/2023', 'DD/MM/YYYY'), 'Грипп', 'Прописаны антибиотики и отдых', 'Температура, кашель', TRUE, 7, 1, 10),
    (TO_DATE('19/10/2023', 'DD/MM/YYYY'), 'Аллергия', 'Назначены антигистаминные препараты', 'Сыпь, зуд', FALSE, 0, 2, 11),
    (TO_DATE('20/10/2023', 'DD/MM/YYYY'), 'Пневмония', 'Назначены антибиотики и режим', 'Высокая температура, боль в груди', TRUE, 10, 3, 1),
    (TO_DATE('20/10/2023', 'DD/MM/YYYY'), 'Травма руки', 'Наложен гипс', 'Упал, болят рука и запястье', TRUE, 14, 4, 2),
    (TO_DATE('21/10/2023', 'DD/MM/YYYY'), 'Гастрит', 'Диета и противовоспалительные препараты', 'Боль в желудке, изжога', FALSE, 0, 5, 3),
    (TO_DATE('21/10/2023', 'DD/MM/YYYY'), 'Мигрень', 'Назначены анальгетики и покой', 'Сильная головная боль, тошнота', TRUE, 5, 6, 4),
    (TO_DATE('22/10/2023', 'DD/MM/YYYY'), 'Операция по удалению аппендикса', 'Экстренная операция', 'Сильная боль в правом боку', TRUE, 1, 7, 5),
    (TO_DATE('22/10/2023', 'DD/MM/YYYY'), 'Зубная боль', 'Назначено лечение и анестезия', 'Пульсирующая боль в зубе', TRUE, 3, 8, 6),
    (TO_DATE('23/10/2023', 'DD/MM/YYYY'), 'Ожог', 'Лечение ожога и перевязка', 'Боль, покраснение кожи', TRUE, 10, 6, 7),
    (TO_DATE('23/10/2023', 'DD/MM/YYYY'), 'Синусит', 'Противовоспалительные препараты и обильное питье', 'Заложенность носа, головная боль', TRUE, 7, 2, 8),
    (TO_DATE('24/10/2023', 'DD/MM/YYYY'), 'Операция по удалению аппендикса', 'Экстренная операция', 'Сильная боль в правом боку', TRUE, 1, 7, 9),
    (TO_DATE('24/10/2023', 'DD/MM/YYYY'), 'Зубная боль', 'Назначено лечение и анестезия', 'Пульсирующая боль в зубе', TRUE, 3, 8, 10),
    (TO_DATE('25/10/2023', 'DD/MM/YYYY'), 'Ожог', 'Лечение ожога и перевязка', 'Боль, покраснение кожи', TRUE, 10, 6, 11),
    (TO_DATE('25/10/2023', 'DD/MM/YYYY'), 'Синусит', 'Противовоспалительные препараты и обильное питье', 'Заложенность носа, головная боль', TRUE, 7, 2, 1),
    (TO_DATE('26/10/2023', 'DD/MM/YYYY'), 'Операция по удалению аппендикса', 'Экстренная операция', 'Сильная боль в правом боку', TRUE, 1, 7, 2),
    (TO_DATE('26/10/2023', 'DD/MM/YYYY'), 'Зубная боль', 'Назначено лечение и анестезия', 'Пульсирующая боль в зубе', TRUE, 3, 8, 3),
    (TO_DATE('27/10/2023', 'DD/MM/YYYY'), 'Ожог', 'Лечение ожога и перевязка', 'Боль, покраснение кожи', TRUE, 10, 6, 4),
    (TO_DATE('27/10/2023', 'DD/MM/YYYY'), 'Синусит', 'Противовоспалительные препараты и обильное питье', 'Заложенность носа, головная боль', TRUE, 7, 2, 5),
    (TO_DATE('28/10/2023', 'DD/MM/YYYY'), 'Операция по удалению аппендикса', 'Экстренная операция', 'Сильная боль в правом боку', TRUE, 1, 7, 6),
    (TO_DATE('28/10/2023', 'DD/MM/YYYY'), 'Зубная боль', 'Назначено лечение и анестезия', 'Пульсирующая боль в зубе', TRUE, 3, 8, 7),
    (TO_DATE('29/10/2023', 'DD/MM/YYYY'), 'Ожог', 'Лечение ожога и перевязка', 'Боль, покраснение кожи', TRUE, 10, 6, 8),
    (TO_DATE('29/10/2023', 'DD/MM/YYYY'), 'Синусит', 'Противовоспалительные препараты и обильное питье', 'Заложенность носа, головная боль', TRUE, 7, 2, 9),
    (TO_DATE('30/10/2023', 'DD/MM/YYYY'), 'Операция по удалению аппендикса', 'Экстренная операция', 'Сильная боль в правом боку', TRUE, 1, 7, 10),
    (TO_DATE('30/10/2023', 'DD/MM/YYYY'), 'Зубная боль', 'Назначено лечение и анестезия', 'Пульсирующая боль в зубе', TRUE, 3, 8, 11),
    (TO_DATE('31/10/2023', 'DD/MM/YYYY'), 'Ожог', 'Лечение ожога и перевязка', 'Боль, покраснение кожи', TRUE, 10, 6, 1),
    (TO_DATE('31/10/2023', 'DD/MM/YYYY'), 'Синусит', 'Противовоспалительные препараты и обильное питье', 'Заложенность носа, головная боль', TRUE, 7, 2, 3);

	
SELECT Patient.address AS "Адрес",
       Visit.visitDate AS "Дата последнего посещения",
       Visit.diagnosis AS "Диагноз"
FROM Patient
JOIN Visit ON Patient.patientID = Patient.patientID
WHERE Patient.surname = 'Лобанов'
ORDER BY Visit.visitDate DESC
LIMIT 1;

SELECT CONCAT(d.surname, ' ', SUBSTRING(d.name, 1, 1), '.', SUBSTRING(d.patronymic, 1, 1), '.') AS doctor_name,
       v.diagnosis AS diagnosis,
       v.visitDate + v.term AS end_date
FROM Doctor d
JOIN Visit v ON d.doctorID = v.doctorID
JOIN Patient p ON v.patientID = p.patientID
WHERE p.surname = 'Поршнев';

SELECT DISTINCT ds.cabinet, ds.receptionDate
FROM DoctorSchedule ds
JOIN Doctor d ON ds.doctorID = d.doctorID
WHERE d.surname = 'Киндий';

SELECT p.surname, p.name, p.patronymic, v.visitDate, v.diagnosis, v.appointments, v.complaints
FROM Patient p
JOIN Visit v ON p.patientID = v.patientID
JOIN Doctor d ON v.doctorID = d.doctorID
WHERE d.surname = 'Крылов' AND (v.visitDate + v.term) >= TO_DATE('25/10/2023', 'DD/MM/YYYY');

SELECT v.appointments
FROM Visit v
JOIN Doctor d ON v.doctorID = d.doctorID
WHERE v.diagnosis = 'Грипп';

SELECT Doctor.surname, Doctor.name, Doctor.patronymic, DoctorSchedule.cabinet
FROM Doctor
JOIN DoctorSchedule ON Doctor.doctorID = DoctorSchedule.doctorID
WHERE DoctorSchedule.receptionDate = TO_DATE('23/10/2023', 'DD/MM/YYYY') -- Укажите нужную дату
AND DoctorSchedule.nameArea = 'Северный округ' -- Укажите нужный район
AND DoctorSchedule.cabinet = 101; -- Укажите нужный кабинет

SELECT COUNT(*) AS total_visits
FROM Visit
JOIN Patient ON Visit.patientID = Patient.patientID
WHERE Patient.surname = 'Лобанов'
AND EXTRACT(MONTH FROM Visit.visitDate) = 10
AND EXTRACT(YEAR FROM Visit.visitDate) = 2023;

SELECT D.surname, D.name, D.patronymic, COUNT(V.visitID) AS numPatients
FROM Doctor D
JOIN DoctorSchedule DS ON D.doctorID = DS.doctorID
JOIN Visit V ON DS.scheduleID = V.doctorID
WHERE V.visitDate >= TO_DATE('01/10/2023', 'DD/MM/YYYY') AND V.visitDate <= TO_DATE('31/10/2023', 'DD/MM/YYYY')
GROUP BY D.surname, D.name, D.patronymic
ORDER BY numPatients DESC;