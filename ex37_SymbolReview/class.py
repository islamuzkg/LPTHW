class MyClass:
	"This is my second class."
	a = 10
	def func(self):
		print "Hello!"
# Output: 10
print(MyClass.a)

# Output: <'function MyClass,func at 0x0000000003079BF8'>
print(MyClass.func)

# Output: "This is my second class.
print(MyClass.__doc__)

print "---------------------After creating a new Class------------------------"
# create a new class MyClass
ob = MyClass()

# Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
print(ob.func)

# Calling function func()
# Output: Hello!
ob.func()
