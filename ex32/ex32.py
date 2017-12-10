# Reference link :https://youtu.be/EDxRFmuTjsc


the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'orange', 'pears', 'apricots', 'bananas']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
	
# same as above

for fruit  in the_count:
	print "A fuit of a type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# We can also build a list, first start with an empty one

elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
	print "Adding %d to the list." % i
	# Range starts at first number (inclusive) 
	# but stops at 1 less than second number (exclusive)
	# This is how items in the list are numbered
	# But 0 as first number is a default, so this can
	# also be written as "range(6)"
	# Can also specify whether range goes up or down
	# and size of steps
	# append is a function that lists understand
	elements.append(i)
	print elements

# now we can print them out too
for i in elements:
	print "Elements was: %d" % i

# this is other way to add to empty list
number = range(6)
for num in number:
	print "This is another way of getting %d" % num
