from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# We could do these two in one line, how?
in_file = open(from_file)
indata = in_file.read()

print "This inout file is %d bytes long" % len(indata)
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue to abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done...."

out_file.close()
in_file.close()
