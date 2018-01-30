ten_things = "Apple Oranges Crows Telephone Light Sugar" # onnitialise string variable

print "Wait there are not ten things in that list. Let's fix that."

stuff = ten_things.split(' ') # split string into list at space, with single quotes.

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"] # initialise list variables with some items

'''
while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

'''
# Alternative to while len(stuff) != 10
for i in range(len(stuff), 10):
	next_one = more_stuff.pop() # removes and returns last item from the list of variable more_stuff
	print "Adding: ", next_one
	stuff.append(next_one) 	# adds returned item from 2nd list to 1st
	print "There are %d items now." % len(stuff) # display length of appended 1st list
	i += 1	# not for while-loop
	
print "There we go: ", stuff

print "Let's do some  things with stuff."

print stuff[1] # displays item at index 1 = 2nd item, because cardinal numbers
print stuff[-1] # displays list item in the list
print stuff.pop()	# removes and returns last item in the list 
print ' '.join(stuff) # merges list items into string with spaces in betweem; 
print '#'.join(stuff[3:5]) # merges items at indicates 3 and 4 (like range(3,5)) with # in between
