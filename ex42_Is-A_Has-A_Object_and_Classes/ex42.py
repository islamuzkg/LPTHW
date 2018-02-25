## Animal is-a abject (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## is-a
class Dog(Animal):
	
	def __init__(self, name):
		## has-a
		self.name = name

## is-a
class Cat(Animal):
	
	def __init__(self, name):
		## has-s
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None

## is-a
class EMployee(Person):
	
	def __init__(self, name, salary):
		
	## has-a (hmm what is this strage magic?)
	super(Employee, self).__init__(name)
	## has-a 
	self.salary = salary

## is-a
class Fish(object):
	pass

## is-a
class Salmon(Fish):
	pass

## is-a
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Satan
satan = Cat("Satan")

## mary is-a Mary
mary = Person("Mary")

## has-a
mary.pet = satan

## is-a
frank = Employee("Frank", 120000)

## has-a
frank.pet = rover

## is-a
flipper = Fish()

## is-a
course = Salmon()

## is-a
course = Salmon()

## is-a
harry = Halibut()

