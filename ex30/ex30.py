# We have assigned below variables to number so we can match them
people = 40
cars = 15
trucks = 30

# With if state below, if cars are greater than pople next line will be printed.
if cars > people:
	print "We should take the cars."
# if cars are less than people then prints elif block.
elif cars < people:
	print "We should not take the cars."
# if neither of them correct, else block will be printed
else:
	print "We can't decide."
	

# Trucks is greated that car, if next print block will be printed.
if trucks > cars:
	print " That's to many trucks."
# Trucks are not less than cars, it will not prin the rest
elif trucks < cars:
		print "May be we could take the trucks."
else:
	print "We still can't decide."
	
# People is greater than trucks, so next will print next line.
if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."


print "---------------------"

# I noticed when I tried to give 2 true if block, that it select
# whatever true statement comes first. 
#
if cars > people or cars < trucks:
	print "That is what I thought"
elif cars < trucks and people > trucks:
	print "Cars are not to big"
elif cars < trucks or people > trucks:
	print "Cars are less bigger"
else:
	print "You tell me"
