# Convert this while-loop to a function that ou can call
# and and replace 6 in the test (i < 6) with a variable.

print "\n Conveting while-loop to a function, drill_1"

def drill_1(n):
	i = 0
	numbers1 = []
	while i < n:
		print "Item %d" % i
		i = i + 1
	print  numbers1

print "nUsing drill_1 with n = 3"
drill_1(3)

print "\nUsing drill_1 with n = 8"
drill_1(8)

# Another variable to the function arguments that you can pass in that
# let =s you change the  + 1 on the line, so you can change how much
# it increments


print "\n Creating function drill_3 to allow variable to step size"
def drill_3(n, s):
	i = 0
	numbers3 = []
	while i < n:
		print "Item: %d" % i
		numbers3.append(i)
		i += s
	print numbers3

print "\nUsing drill_3 with n = 13 and s = 3"
drill_3(12, 3)

'''
Now write it to use for-loops and reange instead. Do you need the 
incrementor in the middle anymore?  What happends if you don't get
rid of it?
'''
print "\ndrill_5 uses a for-loop and range instead"
def drill_5(n, s):
	numbers5 = range(0, n, s)
	# Need to specify starting point of 0 so Python
	# reads the other elements correctly
	for i in numbers5:
		print "Item: %d" % i
	print numbers5

drill_5(14, 4)
































