# ex13.py Parameterd, Unpacking, Variables (I would also call it argument)

from sys import argv # import is used to call a  feature your script

script, first, second, third = argv # holds the arguments you pass to your python script, you can get error when you run your script with less or no arguments when it is required. 

print "The script is called:", script # unpacking the argument
print "Your first variabl is:" first #unpacking the argument
# .....

- arguments: variable values proving by users
- pass: Sending info from arguments to variables
- import: Bringing additional features into Python
- argv: the argument variables
- packing/unpaching values: to get info in and out of argv
- module: the name for the collections of extra code that can be imported into Python

-------------------------------------------------------
# ex14.py  Prompting and Passing 
from sys import argv

script, user_name = argv
promt = '> '

print "Hi %s, I am the %s script." % (user_name, script)
print "Do you like me %s" % user_name
likes = raw_input(promt)
print "You said %r" % likes

- prompt: A character that user can specify to ask for info from the user
-------------------------------------------------------
# ex15.py  Reading Files

- open: Make a file available to Python
- .: dot operator to join a function (or command or method) to an object
- .read: Read the content of the file
- .close: Close the file so it is not longer available to Python 
--------------------------------------------------------
# ex16.py Reading and Writ
- w: write mode
- r: read mode
- a: append mode
- w+: write and read mode
- r+: read and write mode
- .truncate: delets contents of the file
- .write: Write information to the file
- pydoc: import: for infor for inporting
- len(); command that returns the length of string
- readline: Reads just one line of the text file. 
--------------------------------------------------------
# ex17.py More Files
- os.path: a library that adapts the file/directory address to the specific requiments of  the operating system
- exists: a function to determine whether a specific files exists; yields a boolean True or False 

# print "Does the output file exist? %r" % exists(to_file)
# it will print True if the file exists.
--------------------------------------------------------
# ex18.py Names, Variables, Code, Functions
- def: to define custon functions
- (*args): to refer to list of arguments in a function (but better to just list the arguments next to the function name)
- : and intent: to set  block for function











Rference link: https://www.youtube.com/watch?v=8nmekdC2r-c
























