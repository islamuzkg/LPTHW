# Python Object-Oriented Programming
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM

class Employee:
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Islom', 'Alimov', 50000)
emp_2 = Employee('Davud', 'Saliev', 78000)

#print(emp_1)
#print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())	# Here we are calling fullname methode with emp_1 instance

# We can also print the fullname as below
print(Employee.fullname(emp_1))	
