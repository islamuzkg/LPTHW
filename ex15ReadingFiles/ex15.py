# Below code takes the argv file name and open the file reading it. 
# Further down raw_input with prompt "> " will wait for the file name again to open it and print the context of it.

# Imports argv from the sys module
from sys import argv

# Pass the variable script and filename to argv
script, filename = argv

# Opent the filename contained in the argument
txt = open(filename)

# Print out the file's name
print "Here is your file %r: " % filename

# Read the file and thus, print it to the screen
print txt.read()

# Prompt the user to type in the filename again
print "Type the filename again: "
file_again = raw_input("> ")

# Open the entered file and store this action in the txt_again
txt_again = open(file_again)

# Read the lastly entered file context
print txt_again.read()
