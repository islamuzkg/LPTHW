print """
You enter a dark room through below doors. 

Each does will take you to different adventure.
#1 bear
#2 insanity 
#3 media
#4 gym
#5 technology
#6 school
#7 food
#8 animals
"""

door = raw_input("> ")

if door  == "1":
	print "There's a giant bear eating a cheese cake. What do you do?"
	print "1. Taka the cake."
	print "2. Scream at the bear."
	print "3. Lid a fire to scare the bear"
	
	
	bear = raw_input("> ")

	if bear == "1":
		print "Bear eats your face off. Good job!"
	elif bear == "2":
		print "Bear eats your leg off. Good job!"
	elif bear == "3":
		print "That was not bad, now cheese cake is yours."	
	else:
		print "Well doing %s is probably better, Bear runs away." % bear
		

elif door  == "2":
	print "You stare into endless abyss at the Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yello jackets clothespins."
	print "3. Understanding resolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body services powered by a mind of jello. Good job!"
	else: 
		print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
	print """
Where do you usually watch movies or shows?"
1. Youtube
2. Netflix
3. Hulu
4. AMC
"""
    
	media = raw_input("> ")
    
	if media == "1":
		print "Youst know how to search what you watch"
	elif media == "2":
		print "Tired of watching of old stuffs, although they have some cool stuffs to offer"
	elif media == "3":
		print "Must be same as Netflix, not bad"
	elif media == "4":
		print "You must be single"
	else:
		print "You do not like watching movies or shows? You might be doing right thing."

else: 
	print "You stumble around and fall on a knife and die. Good job!"



