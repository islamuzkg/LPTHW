# http://python-textbok.readthedocs.io/en/1.0/Object_Oriented_Programming.html#introduction
# Lists are enclosed in brackets:
# l = [1, 2, "a"]
# Tuples are enclosed in parentheses:
# t = (1, 2, "a")
# Tuples are faster and consume less memory.
# Dictionaries are built with curly brackets:
# d = {"a":1, "b":2}


class Student:
    def __init__(self, name, student_number):
        self.name = name
        self.student_number = sudent_number
        self.classes = []

    def enrol(self, course_running):
        self.classes.append(course_running)
        course_running.add_student(self)


class Department:
    def __init__(self, name, department_code):
        self.name = name
        self.department_code = department_code
        self.courses = {}

    def add_course(self, description, course_code, credits):
        self.courses[course_code] = Course(description, course_code, credits, self)
        return self.courses[course_code]


class Course:
    def __init__(self, description, course_code, credits, department):
        self.description = description
        self.course_code = course_code
        self.credits = credits
        self.department = department
        self.department.add_course(self)

        self.running = []

    def add_running(self, year):
        self.running.append(CourseRunning(self, year))
        return self.running[-1]


class CourseRunning:
    def __init__(self, course, year):
        self.course = course
        self.year = year
        self.students = []

    def add_student(self, student):
        self.students.append(student)


maths_dept = Department("Mathematics and Allplied Mathematics", "MAM")
# print ">>>>> maths_dept", maths_dept
mam1000w = maths_dept.add_course("Mathematics 1000", "MAM1000W", 1)
mam1000w_2013 = mam1000w_add_running(2013)

bob = Student("Bob", "Smith")
bob.enrol(mam1000w_2013)
