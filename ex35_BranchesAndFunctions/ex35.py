from sys import exit
import sys, time

def dead(string):
    print string

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you are not greedy, you win!"
		exit(0)
	else:
		dead("You are greedy bastard!")

def bear_room():
	print "There is a bear hear."
	print "The bear has buch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
			start()
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your legs off.")
		elif choice == "open door" and not bear_moved:
			
			gold_room()
		else:
			print "I got no idea what that means."

def cthulhu_room():
	print "Here you see ugly evil Cthulhu."	
	print "He, it, whatever stares at you and you will go insane."	
	print "Do you flee your life or eat you head?"

	choice = raw_input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasety!")
	else:
		cthulhu_room()
# start function will call other functions and let's user make choice
def start():
	print "You are in a dark room."
	print "There is a door to your back, right and left"
	print "Which one do you take?"

	choice = raw_input("> ") # user's input will be assigned to "choice" variable 
	
	if choice  == "left": # if user says left it will call bear_room function
		bear_room()
	elif choice == "right": # if user says right it will call cthulu_room function
		cthulhu_room()
	elif choice == "back": # choice back is going to take you to the wolf room
		wolf_room()
	else:
		dead("You stumbel around the room untill you starve.")
		exit(0)
# Below finction will take is a wolf_room. Depending of your choice it will take you to bear_room or cthulhu_room.		
def wolf_room(): 
	print """
You see hungry bear."
He is running towards you.
Would you climb  a tree or give him your food?
"""
	choice = raw_input("> ")

	if choice == "give food":
		print "Now run for your life"
		bear_room()
	elif choice == "climb tree":
		print "Well might sit on the for a long time, wolf got some time to wait your you"
		print "\nYou have survived a wolf, now time for cthulhu\n"
		cthulhu_room()
	else:
		print "Waited to much, you dead carrot head"
		exit()
# this function will call other ones as a starting point with the function above
start()
