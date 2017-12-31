from sys import exit
# from colors function we are importing colors listed below, so that we can use it to print in colors.
from colors import green, red, blue
import sys, time

print blue('''
*****************************
Welcome to my Adventure game.
*****************************
''')
print '''
You're standing in an open field west of a white house, with boarded fron door.
A secret path leads to southwest into the forest.
'''
def mailbox():
	print "\nThere is a small mailbox."
	
	choice = raw_input(green("What would you do? \n>>>")) # Here, we are using green() to prompt us in green color.
	
	if choice.lower() == "take mailbox":
		print read("-----------------------------------------------------------")
		print red("Are you serious?")
		print red("Please try again!\n")
		mailbox()
	elif choice.lower() == "open mailbox":
		print red("\nThat's better!")
		read_leaflet()		
	elif choice.lower() == "open door.":
		print red("\nThe door is boarded and you can not remove boards. Please try again.")
		mailbox()
	else:
		print red("\nKeep looking for better option")
		mailbox()

def read_leaflet():
	print red("Opening the mailbox reveals a leaflet.")
	
	choice = raw_input(green("What would you do? \n>>>")) # Here, we are using green() to prompt us in green color.
	
	if choice.lower() == "read leaflet":
		print red("You are on the right track.\n")
		go_north()
	elif choice.lower() == "close mailbox":
		print red("Wow! Did you just ignored the leaflet?")
		read_leaflet()
	elif choice.lower == "throww the leaflet":
		print red("You might want to see what is in there.")
		read_leaflet()
	else:
		 read_leaflet()
def go_north():
	print "You see forest in front of you with trees in all directions to the east, there appears to be the sunlight."
		
	choice = raw_input(green("What would you do? \n>>>")) # Here, we are using green() to prompt us in green color.

	if choice.lower() == "go east":
		print red("The forest becomes impenetrable to the east")
		go_north()
	elif choice.lower() == "go west":
		print red("You would need a machete to go further west.")
		go_north()
	elif choice.lower() == "go south":
		print red("Storm tossed trees blocking you way.")
		go_north()
	elif choice.lower() == "go north":
		print red("Here you go!")
		forest_path()
	else:
		go_north()
	

def forest_path():
	print "You are on the forest path, you should be able to see pile of leaves, trees and one tree has a Jewel-Encrusted Egg Bird's nest."
	
	choice = raw_input(green("What would you do? \n>>>")) # Here, we are using green() to prompt us in green color.
	
	if choice.lower() == "burn leaves":
		print red("Noooooooooooooooo\n")
		forest_path()
	elif choice.lower() == "cut tree":
		print red("Please, I said eggs on the tree.")
		forest_path()
	elif choice.lower() == "climb tree":
		print red("Good, now get the egg from the nest and go back down")
		open_egg()
	else:
		print red("Please read carefully.")
		forest_path()


def open_egg():
	print "\nYou found the egg now. Lets see what we can do wit it!"

	choice = raw_input(green("What would you do? \n>>>")) # Here, we are using green() to prompt us in green color.

	if choice.lower() == "eat egg":
		print red("You can not do that!")
		open_egg()
	elif choice.lower() == "open egg":
		go_house()	
	elif choice.lower == "shake egg":
		print "I would not do that!"
		open_egg()
	else:
		print red("Not sure if that is correct.")
		open_egg()
#-------------------------------------------------------------------------------------------------------------------------------------------
def go_house():
	print "You will find out it is not possible, but it is ok go in to the house using different route."

	choice = raw_input(green("What would you do? \n>>>")) # Here, we are using green() to prompt us in green color.

	if choice.lower() == "go south"
		print red("Now you have to turn left to go around the house")
		go_east()




def go_east():
	print "Now you are on the north side of the house, facing south. you need to turn left and go ...."
	
	choice = raw_input(green("What would you do? \n>>>")) # Here, we are using green() to prompt us in green color.
	
	if choice.lower() == "go east"
		print red("Good, now you can go behind of the house")
		house()


def house():
	print "You have the option to go to the kitchen, leavingroom and attic"


mailbox()
