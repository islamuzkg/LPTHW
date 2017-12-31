loop = 3
while loop == 3:
	print "Let's learn while loop"
	
	choice = raw_input("What do you think?")
	
	if choice.lower() == "yes":
		print "Good choice"
		loop = 4
	else:
		print "You have no choice, you have to do it anyway."
		loop = 5

while loop == 4:
	print "\nThis is from loop == 4"
	break
 
while loop == 5:
	print "\nThis is from loop == 5"
	break


