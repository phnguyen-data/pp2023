def input_students(total):
    for i in range(total):
        print("Input id of student number", i+1, ": ")
        id = input()
        print("Input name of student number", i+1, ": ")
        name = input()
        print("Input dob of student number", i+1, ": ")
        dob = input()

        student_dict = {"id": id, "name": name, "dob": dob}
        students_list.append(student_dict)


def list_students(total):
    for i in range(total):
        print("Id of student number", i + 1, ":", students_list[i]["id"])
        print("Name of student number", i + 1, ":", students_list[i]["name"])
        print("Dob of student number", i + 1, ":", students_list[i]["dob"])


def input_courses(total):
    for i in range(total):
        print("Input name of course number", i+1, ": ")
        course = input()
        course_name_list.append(course)
        print("Input id of course number", i+1, ": ")
        course = input()
        course_id_list.append(course)


def list_courses(total):
    for i in range(total):
        print("Id of course number", i + 1, ":", course_id_list[i])
        print("Name of course number", i + 1, ":", course_name_list[i])


def input_marks(total, m):
    for i in range(total):
        print("Input mark of student number", i+1, "in the course id", m, ": ")
        mark = float(input())
        marks.append(mark)


def list_marks(total, m):
    for i in range(total):
        print("Mark of student number", i+1, "in the course", m, ":", marks[i])


number_of_students = int(input("Input number of students : "))
students_list = []
input_students(number_of_students)
list_students(number_of_students)
number_of_courses = int(input("Input number of courses : "))
course_name_list = []
course_id_list = []
input_courses(number_of_courses)
list_courses(number_of_courses)
ids = input("Input the id of the course you want add marks: ")
marks = []
input_marks(number_of_students, ids)
list_marks(number_of_students, ids)