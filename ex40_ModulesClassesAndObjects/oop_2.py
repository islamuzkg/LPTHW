# Python Object-Oriented Programming
# Reference Link: https://www.youtube.com/watch?v=BJ-VvGyQxho

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

emp_1 = Employee('Isa', 'Mishev', 50000)
emp_2 = Employee('Nano', 'Vimo', 60000)
emp_3 = Employee('Tom', 'Monty', 100000)

# # We can access the last variable frm Class itself and instances
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
#
# # See the differences between  Instance and class itself
# print('Below details are for Employee class etself:')
# print('-' * 30)
# print(Employee.__dict__, '\n')
#
# print('\n')
# print('Dictionary details for intstance emp_1:')
# print('-' * 30)
# print(emp_1.__dict__)
#
# # see how many Employee instances we have
# print('_' * 40, '\n', Employee.num_of_emps)


class Student:

	school_1 = 'Gracie'
	school_2 = '10th Planet'
	def __init__(self, name, rank, years):
		self.name = name
		self.rank = rank
		self.years = years

	def rank_year(self):
		print('_' * 10)
		'''student = "{} is {} and have trainaded {} years."
        print student.format(self.name, self.rank, self.years)'''
		return '%s is %s and have trainaded %d years and trans at %s' % (self.name, self.rank, self.years, self.school_1)

	def school_name(self):
		pass

std_1 = Student('Bruno', 'black', 15)
std_2 = Student('Bred', 'blue', 3)
print std_1.rank_year()
print Student.rank_year(std_2)
print std_1.school_1
