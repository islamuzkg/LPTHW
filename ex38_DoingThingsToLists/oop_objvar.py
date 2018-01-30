# Class And Object Variables
# https://python.swaroopch.com/oop.html
class Robot:
	''''Representing a robot, with a name.'''
	
	#  A class variable, counting the number of robots

	population = 0


	def __init__(self, name):
		'''Initializes  the data.'''
		self.name = name
		print("(Initializing {})".format(self.name))

		# When this person is created, the robot
		# adds to the population
		Robot.population += 1

	def die(self):
		'''I am dying.'''
		print ("{} is being destroyed!".format(self.name))

		Robot.population -= 1
		
		if Robot.population == 0:
			print("{} was the last one.".format(self.name))
		else:
			print("There are still {:d} robots working".format(Robot.population))


	def say_hi(self):
		'''Greeting by the host.

		Yeah, they can fo that.'''
		print("Greetings. my masters call me {}.".format(self.name))

	@classmethod
	def how_many(cls):
		'''Prints the current population.'''
		print('We have {:d} robots.'.format(cls.population))	# {:d}, d is formating caracter. It tells the formatter to treat the aurgument as an integer number and format is as such.


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3P0")
droid2.say_hi()
Robot.how_many()

print("\nRobots have finished their work. So let's destroy them")
droid1.die()
droid2.die()

Robot.how_many()
print(Robot.say_hi.__doc__)
