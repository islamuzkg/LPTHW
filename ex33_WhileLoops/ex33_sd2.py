'''
Here are three main choices here, so let's 
define a  finction for each of those items.
This way, our menu code remains really simple 
even as we add more complecated code to the 
actions of riding a bicycle, going for a run, 
or climbing a mountain.
'''
def ride_bicycle():
	print "\nHere's a bicycle. Have fun!\n"

def go_running():
	print "\nHere are some running shoes. Run fast!\n"

def climb_mount():
	print "\nHere is a map. Can you leave a trip plan for us?\n"

print "\nWelcome to the nature center. What would you like to do?"

choice = ''

while choice != 'q':
	print "\n[1] Enter 1 to take a bicycle ride."
	print "[2] Enter 2 to go for a run."
	print "[3] Enter 3 to climb a mountain."
	print "[q] Enter q to quit"
	
	choice = raw_input("\nWhat would you like to do?\n> ")
	if choice == '1':
		ride_bicycle()
	elif choice == '2':
		go_running()
	elif choice == '3': 
		climb_mount()
	elif choice == 'q':
		print "\nThanks for paying. See you later. \n"
	else:
		print "\nI don't understand that choice, please try again. \n"

