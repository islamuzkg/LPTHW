# Object oriented programming explained
# https://python.swaroopch.com/oop.html

class Person:
    def __init__(self, name):
	self.name = name


    def say_hi(self):
        print ('Hello, how are you!', self.name)

p = Person('Islom')
p.say_hi()
