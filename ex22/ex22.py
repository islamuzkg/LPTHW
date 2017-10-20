# ex13.py Parameterd, Unpacking, Variables (I would also call it argument)

from sys import argv # import is used to call a  feature your script

script, first, second, third = argv # holds the arguments you pass to your python script, you can get error when you run your script with less or no arguments when it is required. 

print "The script is called:", script # unpacking the argument
print "Your first variabl is:" first #unpacking the argument
# .....

# ex14.py  Prompting and Passing 
from sys import argv

script, user_name = argv
promt = '> '

print "Hi %s, I am the %s script." % (user_name, script)
print "Do you like me %s" % user_name
likes = raw_input(promt)
print "You said %r" % likes
