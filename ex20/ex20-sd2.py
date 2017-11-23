from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
def rewind(f):
	f.seek(0)
def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "I. First let's print whole file: \n"

print_all(current_file)
rewind(current_file)
print_all(current_file)
rewind(current_file)
print_all(current_file)

#print "II. Now let's rewind, kind of like a tape.\n"
#rewind(current_file)

#print "III. Let's print three line:\n"

#current_line = 0 
#print "Current line:", current_line
#print_a_line(current_line, current_file)

#current_line = current_line + 1
#print "Current line:", current_line
#print_a_line(current_line, current_file)

#current_line = current_line + 1
#print "Current line:", current_line
#print_a_line(current_line, current_file)
