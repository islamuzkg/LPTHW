from sys import argv

script, filename = argv

print "We're gaoing to erase %r."  % filename
print "If you don't want that. hit CTRL-C (^C)."
print "IF you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."

target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "Now I'm going to write these to the file."

target_formatter = "%s %s %s %s %s %s"
formatted_lines = target_formatter % (line1, "\n", line2, "\n", line3, "\n") 
target.write(formatted_lines)

target = open(filename)
read_file = target.read() 

print read_file
print read_file
print "And finally, we can close it."
target.close()
