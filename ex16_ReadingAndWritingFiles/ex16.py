# argv is a list containing the arguments passed to python interpreter when called from command line
from sys import argv

# Generally, the first argument to a command line executable is a script name, and the rest are the expected arguements. 
script, filename = argv

# Prints lines inside of quotation marks. 
print "We're going to earase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you don't want that, hit RETERN."

# As python lets you to interact with outside of the world to get input. The "raw_input" finction waits user to type some input and press return. It then get whatever was typed to process.
raw_input("?")

print "Opening the file..."

#  Open function opens a file storing the output value in the variable called target. See more details in the next comment.
target = open(filename, 'a')

print "Truncating the file. Goodbye!"
# This truncate function remove the content of the file, but if we use the open funtion wwith (r/r+w) read and write modes it will remove the content of the file overwriting into the file (depending on the permission of the file) unless we use (a) mode which appends to the file.
target.truncate()

print "Now I am going to ask you these three lines"

# raw_input function waits user to type assing the value to variable after you press return
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ") 
line3 = raw_input("line 3: ")

print "Iam goin to write these to the file."

# write() function writes each line to the file, and ("\n") will break to the new line.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finanly, we can close it."
# Finally close the file.
target.close()
