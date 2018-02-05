# Python Object-Oriented Programming
# Regular, class, static methods
# Reference Link: https://youtu.be/rq8cL2XMM5M


class Employee:
	
	# class variable can be used by all methods/functions within this lass
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

