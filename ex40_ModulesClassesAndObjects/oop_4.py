# Python Object-Oriented Programming
# Subclasses
# Reference Link: https://youtu.be/RSl87lqOXDE


class Employee:
	
	# class variable can be used by all methods/functions within this lass
	num_of_emps = 0
	raise_amount = 1.04
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
	
		Employee.num_of_emps += 1
		
	def fullname(self): 
		return '{} {}'.format(self.first, self.last) 

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount) 

class Developer(Employee): # Developer subclass, it can inherit methods from parent (Employee class)
	raise_amount = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay) # super is for parent class name. # This line gave me following (TypeError: super() takes at least 1 argument (0 given)) in Python2 but Python3ZZ
		self.prog_lang = prog_lang

class Manager(Employee):  # Manager subclass, it can inherit methods from parent (Employee class)
	
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay) # This line gave me following (TypeError: super() takes at least 1 argument (0 given)) in Python2 but Python3
		if employees is None:
			self.empployees = []
		else:
			self.employees = employees
	
	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)
	
	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)	

	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname())

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Tom', 'Jerrey', 60000, 'Java') 


#print(dev_1.email)
#print(dev_2.email)

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)

#print(dev_2.prog_lang)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.print_emps()
