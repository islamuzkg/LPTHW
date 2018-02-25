# Python Object-Oriented Programming
# Regular, class, static methods
# Reference Link: https://www.geeksforgeeks.org/class-method-vs-static-method-python/


# Python program to demonstrate
# use of class method and static method.
from datetime import date
class Person():
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	# a classmethod to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)
	
	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print person1.age
print person2.age

# print the result

print Person.isAdult(22)

















"""
class Employee:

	# class variable can be used by all methods/functions within this class
	num_of_emps = 0
	raise_amount = 1.4

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1

	def fullname(self): # method function to get full name
		return '{} {}'.format(self.first, self.last) # will combines two variable names

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount) # we could also use Employee.raise_amount Using the class variable raise_amount

	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount

	# Below class method is alternative constructor for below
	# first, last, pay = emp_str_1.split('-')
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

emp_1 = Employee('Isa', 'Mishev', 50000)
emp_2 = Employee('Nano', 'Vimo', 60000)
emp_3 = Employee('Tom', 'Monty', 100000)

# Parsingt the Employee information from string  saperated with hyphen (-)
emp_str_1 = 'John-Doe-75000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_1 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_1.email)
print(new_emp_2.pay)
print(new_emp_1.fullname())


# Using thie class method to raise_amount
Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
"""
#
# class Student:
#
# 	school_1 = 'Gracie'
# 	school_2 = '10th Planet'
#
# 	def __init__(self, name, rank, years):
# 		self.name = name
# 		self.rank = rank
# 		self.years = years
#
# 	def rank_year(self):
# 		print('_' * 10)
# 		'''student = "{} is {} and have trainaded {} years."
#         print student.format(self.name, self.rank, self.years)'''
# 		return '%s is %s and have trainaded %d years and trans at %s' % (self.name, self.rank, self.years, self.school_1)
#
# 	def school_name(self):
# 		pass
#
# std_1 = Student('Bruno', 'black', 15)
# std_2 = Student('Bred', 'blue', 3)
