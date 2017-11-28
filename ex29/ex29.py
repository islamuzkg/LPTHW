people = 20
cats = 30
dogs = 15

#For if statements, structure is similar to "def," with colon at the end of the 1st line, then intent

if people < cats:
	# 20 < 30 is true, so this will print
	print "Too many cats! The world is doomed!"

if people > cats:
	# 20 > 30 is false, so this will not will print
	print "Not many cats! The world is saved!"

if people < dogs:
	# 20 < 15 is false, so this will not print
	print "The world is drooled on!"
if people > dogs:
	# 20 > 15 is true, so this will print
	print "World is dry!"

dogs += 5
# dogs = 15 + 5 = 20
# This is a method for incrementing numbers
# It is equivalent to "dogs = dogs + 5"
# You can also use -=, *=, /=. etc.

if people >= dogs:
	# 20 >= 20 is true, so this will print
	print "People are graeted than or eaqual to dogs."

if people <= dogs:
	# 20 <= 20 is true, so this will print
	print "People are less than or qual to dogs."

if people == dogs:
	# 20 == 20 is true, so this will print
	print "People are dogs."

Reference Link: https://www.youtube.com/watch?v=yZHPUvoSKeA
