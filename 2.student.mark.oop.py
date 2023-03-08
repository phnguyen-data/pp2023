class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def input_info(self, i):
        print("Input id of student", i+1, ": ")
        self.id = input()
        print("Input name of student", i+1, ": ")
        self.name = input()
        print("Input dob of student", i+1, ": ")
        self.dob = input()

    def display_info(self):
        print("Id of student", i+1, ":", self.id)
        print("Name of student", i+1, ":", self.name)
        print("Dob of student", i+1, ":", self.dob)

    def input_marks(self, course_id):
        mark = float(input("Input mark for course {}: ".format(course_id)))
        self.marks[course_id] = mark

    def display_marks(self):
        for course_id, mark in self.marks.items():
            print("Mark for course {}: {}".format(course_id, mark))


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.marks = {}

    def input_info(self):
        self.id = input("Input id of course: ")
        self.name = input("Input name of course: ")

    def display_info(self):
        print("Id of course:", self.id)
        print("Name of course:", self.name)

    def input_marks(self, students):
        for student in students:
            mark = float(input("Input mark for student {}: ".format(student.id)))
            self.marks[student.id] = mark

    def display_marks(self):
        for student_id, mark in self.marks.items():
            print("Mark for student {}: {}".format(student_id, mark))


number_of_students = int(input("Input number of students : "))
students = []
for i in range(number_of_students):
    student = Student("", "", "")
    student.input_info(i)
    students.append(student)
for i in range(number_of_students):
    student.display_info()

number_of_courses = int(input("Input number of courses : "))
courses = []
for i in range(number_of_courses):
    course = Course("", "")
    course.input_info()
    courses.append(course)
for course in courses:
    course.display_info()
course_id = input("Input the id of the course you want to add marks: ")
for course in courses:
    if course.id == course_id:
        course.input_marks(students)
        course.display_marks()
        break
