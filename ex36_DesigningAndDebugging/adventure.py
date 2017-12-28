from sys import exit
# from colors function we are importing colors listed below, so that we can use it to print a prompt in color
from colors import green, red, blue
import sys, time

print '''
*****************************
Welcome to my Adventure game.
*****************************

You're standing in an open field west of a white house, with boarded fron door.
A secret path leads to southwest into the forest.
'''
def mailbox():
	print "There is a small mailbox."
	
	choice = raw_input(green("What would you do? \n>>>")) # Here,we are using green() to prompt us in green color.
	
	if choice.lower() == "take mailbox":
		print "-----------------------------------------------------------"
		print "Are you serious?"
		print "Please try again!\n"
		mailbox()
	if choice.lower() == "open mailbox":
		print "\nThat's better."
	if choice.lower() == "open door.":
		print "\nThe door is boarded and you can not remove boards. Please try again."
		mailbox()
mailbox()
