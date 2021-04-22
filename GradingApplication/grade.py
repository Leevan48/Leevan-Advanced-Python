import pandas as pd
import mysql.connector
db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="grading_application"
)


class Grades:
    def __init__(self,Student_id, Course_id, Grade ):
        self.grade = Grade
        self.student_id = Student_id
        self.course_id = Course_id

    def __str__(self):
        return  "[Student ID: " + str(self.student_id) + " Course ID: " + str(self.course_id) + " Grade: " + str(self.grade) + "] "

    def update(self, Student_id, Courses_id, Grade):
        cursor = db.cursor()
        sql =  "UPDATE student_has_courses SET Grade=%s WHERE Student_id=" + str(Student_id) + " and Courses_id=" + str(Courses_id)
        data = (Grade,)
        cursor.execute(sql, data)
        db.commit()


class GradeRepository:

    @staticmethod
    def get_grade_object(db_row):
        grade = Grades(db_row[0], db_row[1], db_row[2])
        return grade

    @staticmethod
    def get_grade(Student_id, Courses_id):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM students_has_courses WHERE Student_id=" + str(Student_id) + " and Courses_id=" + str(Courses_id))
        result = cursor.fetchone()
        if result:
            grade = GradeRepository.get_grade_object(result)
            return grade
        else:
            return None

    @staticmethod
    def all_grades():
        cursor = db.cursor()
        grades = {}
        cursor.execute("SELECT * FROM student_has_courses")
        result = cursor.fetchall()
        for row in result:
            grade = GradeRepository.get_grade_object(row)
            grades[grade.student_id, grade.course_id] = grade
        return grades

    @staticmethod
    def add_grade(Grade, Student_id, Courses_id):
        cursor = db.cursor()
        sql = "INSERT INTO student_has_courses(Student_id, Courses_id, Grade) VALUES (%s, %s, %s)"
        data = (Student_id, Courses_id, Grade)
        cursor.execute(sql, data)
        db.commit()

    @staticmethod
    def update_grade(Grade, Student_id, Courses_id):
        cursor = db.cursor()
        sql = "UPDATE student_has_courses SET Grade=%s WHERE Student_id=%s and Courses_id=%s"
        data = (Grade, Student_id, Courses_id)
        cursor.execute(sql, data)
        db.commit()

    @staticmethod
    def view_students_grades(Student_id):
        cursor = db.cursor()
        students_grades = {}
        cursor.execute("SELECT s.fullname, s.id, co.title, co.id, shc.grade FROM student_has_courses shc LEFT JOIN student s on s.id = shc.Student_id LEFT JOIN courses co on co.id = shc.Courses_id WHERE s.id =" + str(Student_id))
        result = cursor.fetchall()

        for row in result:
            students_grades[row[2]] = row[4]

        return students_grades

    @staticmethod
    def export_grades():
        cursor = db.cursor()
        cursor.execute("SELECT * FROM student_has_courses")
        result = cursor.fetchall()

        df = pd.DataFrame(result)
        df.columns = ["Student ID", "Course ID", "Grade"]
        df.set_index('Student ID')
        df.to_csv(r'C:\Users\tnaidoo\Desktop\Leevan-Advanced-Python\GradingApplication\grades.csv', index=False)

    @staticmethod
    def export_student_grades(Student_id):
        cursor = db.cursor()
        cursor.execute("SELECT s.fullname, s.id, co.title, co.id, shc.grade FROM student_has_courses shc LEFT JOIN student s on s.id = shc.Student_id LEFT JOIN courses co on co.id = shc.Courses_id WHERE s.id =" + str(Student_id))
        result = cursor.fetchall()

        df = pd.DataFrame(result)
        df.columns = ["Full Name", "Student ID", "Course Title", "Course ID", "Grade"]
        df.set_index('Student ID')
        df.to_csv(r'C:\Users\tnaidoo\Desktop\Leevan-Advanced-Python\GradingApplication\student_grades.csv', index=False)



