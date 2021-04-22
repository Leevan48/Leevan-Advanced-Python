from faker import Faker
import random
MAJORS = ['Engineering', 'Medicine', 'Psychology', 'Social Science', 'Business']
COURSES = {
    'Engineering': ['Intro to Software Engineering','Computer Organization', 'Applied Algorithms', 'Systems Programming', 'Discrete Math'],
    'Medicine': ['Anatomy', 'Pharmacology', 'Microbiology', 'Clinical Skills', 'Population Health'],
    'Psychology': ['Biopsychology', 'Environmental Science', 'English Communication', 'Intro to Psychology', 'Social Psychology'],
    'Social Science': ['Anthropology', 'Economics', 'Environment & Society', 'Labour Studies', 'Politics'],
    'Business': ['Marketing', 'Law', 'Microeconomics', 'Macroeconomics', 'HR management']
}

import mysql.connector
db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="grading_application"
)

fake_data = Faker()

cursor = db.cursor()

# for _ in range(20):
#
#
#     sql = "INSERT INTO student(fullname, major, age, working, native) VALUES (%s, %s, %s, %s, %s)"
#     working = random.randint(0,1)
#     native = random.randint(0,1)
#     x = random.randint(0,4)
#     age = random.randint(17, 30)
#     major = MAJORS[x]
#     data = (fake_data.name(), major, age, working, native)
#     cursor.execute(sql, data)
#
#     sq = "INSERT INTO courses(title, liberal, credits) VALUES (%s, %s, %s)"
#     liberal = random.randint(0, 1)
#     credits = random.randint(1, 4)
#     number = random.randint(0, 4)
#     title = COURSES[major][number]
#     dat = (title, liberal, credits)
#     cursor.execute(sq, dat)


for _ in range(20):
    sql = "INSERT INTO student_has_courses(Student_id, Courses_id, Grade) VALUES (%s, %s, %s)"
    Student_id = random.randint(1,20)
    Courses_id = random.randint(1, 20)
    Grade = random.randint(0, 100)
    data = (Student_id, Courses_id, Grade)
    cursor.execute(sql, data)


db.commit()
