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

class Developer(Employee):
	raise_amount = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay) # super is for parent class name
		self.prog_lang = prog_lang


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Tom', 'Jerrey', 60000, 'Java') 

#print(dev_1.email)
#print(dev_2.email)

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)

print(dev_2.prog_lang)
