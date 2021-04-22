import pandas as pd
import mysql.connector
db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="grading_application"
)


class Students:

    def __init__(self, id, fullname, major,  age, working, native):
        self.student_id = id
        self.fullname = fullname
        self.age = age
        self.working = working
        self.native = native
        self.major = major

    def __str__(self):
        return '[ ID: ' + str(self.student_id)  \
              + ' Full Name: ' + str(self.fullname) \
              + ' Age: ' + str(self.age) \
              + ' Major: ' + str(self.major) \
              + ' Working: ' + str(self.working) \
              + ' Native: ' + str(self.native) \
              + ' ]'



class StudentRepository:

    @staticmethod
    def get_student_object(db_row):
        student = Students(db_row[0], db_row[1], db_row[2], db_row[3], db_row[4], db_row[5])
        return student

    @staticmethod
    def get_student(id):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM student WHERE id=" + str(id))
        result = cursor.fetchone()
        if result:
            student = StudentRepository.get_student_object(result)
            return student
        else:
            return None

    @staticmethod
    def all_students():
        cursor = db.cursor()
        students = {}
        cursor.execute("SELECT * FROM student")
        result = cursor.fetchall()
        for row in result:
            student = StudentRepository.get_student_object(row)
            students[student.student_id] = student
        return students

    @staticmethod
    def add_new(fullname, major, age, working, native):
        cursor = db.cursor()
        sql = "INSERT INTO student(fullname, major, age, working, native) VALUES (%s, %s, %s, %s, %s)"
        data = (fullname, major, age, working, native)
        cursor.execute(sql, data)
        db.commit()

    @staticmethod
    def update(id, fullname, major, age, working, native):
        cursor = db.cursor()
        sql = "UPDATE student SET fullname=%s, major=%s, age=%s, working=%s, native=%s WHERE id=%s"
        data = (fullname, major, age, working, native, id)
        cursor.execute(sql, data)
        db.commit()

    @staticmethod
    def export_students():
        cursor = db.cursor()
        cursor.execute("SELECT * FROM student")
        result = cursor.fetchall()
        df = pd.DataFrame(result)
        df.columns = ["ID", "Full Name", "Age", "Major", "Working", "Native"]
        df.set_index('ID')
        df.to_csv(r'C:\Users\tnaidoo\Desktop\Leevan-Advanced-Python\GradingApplication\students.csv', index=False)