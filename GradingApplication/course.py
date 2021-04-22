import pandas as pd
import mysql.connector
db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="grading_application"
)

class Courses:
    def __init__(self, id,  title, liberal, credits):
        self.course_id = id
        self.title = title
        self.liberal = liberal
        self.credits = credits

    def __str__(self):
        return self.title + " [Liberal: " + \
               str(self.liberal) + ", Credits: " \
               + str(self.credits)  + "]"

    def update(self, title, liberal, credits):
        cursor = db.cursor()
        sql = "UPDATE courses SET title=%s, liberal=%s, credits=%s WHERE id=" + str(self.course_id)
        data = (title, liberal, credits)
        cursor.execute(sql, data)
        db.commit()

class CoursesRepository:

    @staticmethod
    def get_course_object(db_row):
        course = Courses(db_row[0], db_row[1], db_row[2], db_row[3])
        return course

    @staticmethod
    def get_course(id):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM courses WHERE id=" + str(id))
        result = cursor.fetchone()
        if result:
            course = CoursesRepository.get_course_object(result)
            return course
        else:
            return None

    @staticmethod
    def all_courses():
        cursor = db.cursor()
        courses = {}
        cursor.execute("SELECT * FROM courses")
        result = cursor.fetchall()
        for row in result:
            course = CoursesRepository.get_course_object(row)
            courses[course.course_id] = course
        return courses

    @staticmethod
    def add_new(title, liberal, credits):
        cursor = db.cursor()
        sql = "INSERT INTO courses(title, liberal, credits) VALUES (%s, %s, %s)"
        data = (title, liberal, credits)
        cursor.execute(sql, data)
        db.commit()

    @staticmethod
    def export_courses():
        cursor = db.cursor()
        cursor.execute("SELECT * FROM courses")
        result = cursor.fetchall()
        df = pd.DataFrame(result)
        df.columns = ["ID", "Title", "Liberal", "Credits"]
        df.set_index('ID')
        df.to_csv(r'C:\Users\tnaidoo\Desktop\Leevan-Advanced-Python\GradingApplication\courses.csv', index=False)