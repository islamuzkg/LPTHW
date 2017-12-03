# Apologize for spelling mistake, please, just don't tell my wife
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


elif door == "4":
	print "Where do you go for exercises?"
	print "1. Martial Art"
	print "2. Lifting"
	print "3. Gymnastics."
	print "4. Swimming"
	
	gym = raw_input("> ")
	
	if gym == "1" or gym == "2":
		print "Sport must be part of your lifestyle."
		
		print "\nWhat kinda sport do you like?"
		print "1. Self defense."
		print "2. Bodybuilding"
		
		sport = raw_input("> ")
		
		if sport == "1":
			print "Be water my friend."
		elif sport == "2":
			print "Make sure you don't skip the leg day."
		else: # it is printing else block as well when if 1st if block is true
			print "Any sport is better than nothing!"
		
	elif gym == "3" or gym == "4":
		print "Healthy body will have healthy mind!"
		
		print "\n Please tell us which one you like? \n1. Gymnastics \n2. Swimming"
		
		sport = raw_input("> ")
		if sport == "1":
			print "You are flexible person."
		elif sport == "2":
			print "You must swim like a wish."
		else: 
			print "You are busy with something else"
		
	
	else:
		print "You are missing a lot"
	

elif door == "5":
	print "\nWhich of these phones do you have" 
	print "\n1. Iphone \n2. Android \n3 Google phone"
	
	tech = raw_input("> ")
	if tech == "1":
		print "You are fan of Steve Job."
	elif tech == "2":
		print "You lke your freedom."
	elif tech == "3":
		print "like to try new stuffs?"
	else:
		print "You dont chase the brand, smart one"


elif door == "6":

	print "\n What is your highest level of education"
	print """
1. High school.
2. Bachelor's degree.
3. Master degree.
"""
	school = raw_input("> ")
	
	if school == "1":
		print "You have some way to go for success."
	elif school == "2":
		print "You might be thinking, if you need start working or continue to master degree."
	elif school == "3":
		print "You are pretty settled, and looking for a job."
	else:
		print "Education is important, hope you have a plan"

elif door == "7":
	print "How do you get you protain?"
	print  """
1. Beef
2. Chicken
3. Fish
4. veggie
"""
	food = raw_input("> ")
	
	if food == "1":
		print "You're a meat lover"
	elif food == "2":
		print "Healthy option, that sounds good."
	elif food == "3":
		print "It is realy good stuff, I bet you love sushi."
	elif food == "4":
		print "It is the best way to stay lean and fit."
	else: 
		print "Protain is important for your body."

elif door == "8":
	print "What is you fave animal?"
	print """
1. cat
2. dog
"""
	animal = raw_input("> ")
	if animal == "1" or animal == "2":
		print "You have very kind heard!"
	else:
		print "please enter animal name you like, else just say no. No judging."
		animal_name = raw_input("> ")
		if animal_name == "NO" or animal_name == "no":
			print "It is ok, no judging"
		elif animal_name == "No":
			print "It is ok, no judging"
		else:
			print "%s is cool one" % animal_name
else: 
	print "You stumble around and fall on a knife and die. Good job!"



