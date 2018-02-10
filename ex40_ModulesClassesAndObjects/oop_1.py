# Python Object-Oriented Programming
# Reference Link: https://www.youtube.com/watch?v=ZDa-Z5JzLYM
class Employee:

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'


	def fullname(self): # method function to get full name
		return '{} {}'.format(self.first, self.last) # will combines two variable names

emp_1 = Employee('Isa', 'Mishev', 50000)
emp_2 = Employee('Nano', 'Vimo', 60000)

#print(emp_1.email)
#print(emp_2.email)

# Bellow lines give same output
#print(emp_1.fullname())

#print(Employee.fullname(emp_1))

class Student:

	def __init__(self, name, rank, years):
		self.name = name
		self.rank = rank
		self.years = years

	def rank_year(self):
		print('_' * 10)
        #return '{} is {} and have trainaded {} years'.format(self.name, self.rank, self.years)
		return '%s is %s and have trainaded %d years' % (self.name, self.rank, self.years)

std_1 = Student('Bruno', 'black', 15)
std_2 = Student('Bred', 'blue', 3)

print(std_1.name)
print(Student.rank_year(std_1))
