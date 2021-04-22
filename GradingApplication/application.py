from student import *
from course import CoursesRepository
from grade import *
import pandas as pd


def select_menu():
    print("\n MENU")
    print("1. View Students")
    print("2. Add Student")
    print("3. Update Student")
    print("4. View Courses")
    print("5. Add Course")
    print("6. Add Grade")
    print("7. Update Grade")
    print("8. View Student's Grades")
    print("9. View ALL Grades")
    print("0. EXIT")
    try:
        action = int(input("> "))
        return action
    except ValueError:
        return -1

#STUDENT METHODS


def display_students(student):

    for id in student:
        print(student[id])

    answer = input("Do you want to save this data in a csv file? Enter (Y) for yes and (N) for no ")
    if answer == "Y":
        StudentRepository.export_students()
    elif answer == "N":
        pass



def add_student():
    fullname = input("Name: ")
    try:
        major = input("Major: ")
        age = int(input("Age: "))
        working = int(input("Working ( 1 = working, 0 = not working) :"))
        native =  int(input("Native ( 1 = native, 0 = non-native) :"))
    except (ValueError):
        print("Wrong value")
        return
    StudentRepository.add_new(fullname, major, age, working, native)


def update_student():
    id = int(input("ID: "))

    fullname = input("Name: ")

    try:
        major = input("Major: ")
        age = int(input("Age: "))
        working = int(input("Working ( 1 = working, 0 = not working) :"))
        native = int(input("Native ( 1 = native, 0 = non-native) :"))
    except (ValueError):
        print("Wrong value")
        return
    StudentRepository.update(id, fullname, major, age, working, native)

# COURSES METHODS


def display_courses(courses):
    for id in courses:
        print(courses[id])

    answer = input("Do you want to save this data in a csv file? Enter (Y) for yes and (N) for no ")
    if answer == "Y":
        CoursesRepository.export_courses()
    elif answer == "N":
        pass


def add_course():
    title = input("Title: ")
    try:
        liberal = input("Liberal: ")
        credits = int(input("Credits: "))
    except (ValueError):
        print("Wrong value")
        return
    CoursesRepository.add_new(title, liberal, credits)

# GRADE METHODS


def add_grade():

    try:
        Student_id = int(input("Student ID: "))
        Courses_id = int(input("Courses ID: "))
        Grade = int(input("Grade: "))
    except (ValueError):
        print("Wrong value")
        return
    GradeRepository.add_grade(Grade, Student_id, Courses_id)

def update_grade():
    try:
        Student_id = int(input("Student ID: "))
        Courses_id = int(input("Courses ID: "))
        Grade = int(input("Grade: "))
    except (ValueError):
        print("Wrong value")
        return
    GradeRepository.update_grade(Grade, Student_id, Courses_id)

def view_students_grades():
    try:
        Student_id = int(input("Student ID"))
    except (ValueError):
        print("Wrong value")
        return
    students_grades = GradeRepository.view_students_grades(Student_id)

    for course in students_grades:
        print(course, students_grades[course])

    answer = input("Do you want to save this data in a csv file? Enter (Y) for yes and (N) for no ")
    if answer == "Y":
        GradeRepository.export_student_grades(Student_id)
    elif answer == "N":
        pass


def display_grades(grade):
    for Grade in grade:
        print(grade[Grade])

    answer = input("Do you want to save this data in a csv file? Enter (Y) for yes and (N) for no ")
    if answer == "Y":
        GradeRepository.export_grades()
    elif answer == "N":
        pass


if __name__ == '__main__':
    while True:
        action = select_menu()
        if action == 1:
            students = StudentRepository.all_students()
            display_students(students)
        elif action == 2:
            add_student()
        elif action == 3:
            update_student()
        elif action == 4:
            courses = CoursesRepository.all_courses()
            display_courses(courses)
        elif action == 5:
            add_course()
        elif action == 6:
            add_grade()
        elif action == 7:
            update_grade()
        elif action == 8:
            view_students_grades()
        elif action == 9:
            grades = GradeRepository.all_grades()
            display_grades(grades)
        elif action == 0:
            print("Bye!")
            break
        else:
            print("Invalid action")
        input("any key to continue ...")