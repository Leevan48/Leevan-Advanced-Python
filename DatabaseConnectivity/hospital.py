import mysql.connector
db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="hospital"
)


class Hospital:
    def __init__(self, id, name, beds, available):
        self.id = id
        self.name = name
        self.beds = beds
        self.available = available

    def __str__(self):
        return self.name + " [beds: " + \
               str(self.beds) + ", avail: " \
               + str(self.available) + "]"

    def update(self, beds, available):
        cursor = db.cursor()
        sql = "UPDATE hospitals SET beds=%s, available=%s WHERE id=" + str(self.id)
        data = (beds, available)
        cursor.execute(sql, data)
        db.commit()

class HospitalRepository:

    @staticmethod
    def get_hospital_object(db_row):
        hospital = Hospital(db_row[0], db_row[1], db_row[2], db_row[3])
        return hospital

    @staticmethod
    def get_hospital(id):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM hospitals WHERE id=" + str(id))
        result = cursor.fetchone()
        if result:
            hospital = HospitalRepository.get_hospital_object(result)
            return hospital
        else:
            return None

    @staticmethod
    def all_hospitals():
        cursor = db.cursor()
        hospitals = {}
        cursor.execute("SELECT * FROM hospitals")
        result = cursor.fetchall()
        for row in result:
            hospital = HospitalRepository.get_hospital_object(row)
            hospitals[hospital.id] = hospital
        return hospitals

    @staticmethod
    def add_new(name, beds, available):
        cursor = db.cursor()
        sql = "INSERT INTO hospitals(name, beds, available) VALUES (%s, %s, %s)"
        data = (name, beds, available)
        cursor.execute(sql, data)
        db.commit()