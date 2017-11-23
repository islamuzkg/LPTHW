# Importing argv from the sys module
from sys import argv

# Pass the variables input_file and script to argv
script, input_file = argv

# Define find "print_all" with parameter "f"
def print_all(f):
	# Prints complete content of the pased file 
	print f.read()
# Define function "rewind" with parameter "f"
def rewind(f):
	# Put the file pointer back to position 0
	# which is the begining of the file
	f.seek(0)
# Define function "print_a_line" with 2 parameters: line_count and f
def print_a_line(line_count, f):
	# Print the line number, followed by the line itself
	print line_count, f.readline()

# Open the file object and store it in current_file
current_file = open(input_file)

# Tell user, the whole file gets printed
print "I. First let's print whole file: \n"

# Output the complete file calling the function below with its parameters
print_all(current_file)

# Tell the user, the file cursor gets rewinded
print "II. Now let's rewind, kind of like a tape.\n"
# Call rewind finction with uses seek(0) to return the pointer to posision 0
rewind(current_file)

# Tell user 3 lines are going to be printed
print "III. Let's print three line:\n"

# Store the current line by 1
current_line = 1
# Execute print_a_line function
print_a_line(current_line, current_file)

# Increment current line by 1
current_line += 1
# Execute print_a_line function
print_a_line(current_line, current_file)

# Increment current line by 1
current_line += 1
# Execute print_a_line function
print_a_line(current_line, current_file)
