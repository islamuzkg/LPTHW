
# ex01.py "A Good First Program"
- print: Display text in counsole

----------------------------------------------------
# ex02.py "Comments And POund Characters"
- #: Comment/diable a line

-----------------------------------------------------
# ex03.py
- + plus
- - minus
- / slash
- * asterisk
- %  percent (but used as modulo/modules_dict)
- < less-than
- > greater-than
- <+ less-than-equal
- >= greater-than-equal
Per https://www.youtube.com/watch?v=8nmekdC2r-c, the "modulus" is not the remainder; it's the divisor used as a basis for determining the remainder.... "Modulo" is the relational term modulus, 
and we use it to briefly state a number is being taken with a certain modules: a mod b (read "a modulo b")

-----------------------------------------------------
# ex04.py "Variables and Names" 
- _: underscore in variable names
	There are 5 cases for using the underscore in Python.
* For storing the value of last expression in interpreter.
* For ignoring the specific values. (so-called “I don’t care”)
* To give special meanings and functions to name of vartiables or functions, also treat it as private variable
* To use as ‘Internationalization(i18n)’ or ‘Localization(l10n)’ functions.
* To separate the digits of number literal value.


- floating point:  numbers with decimals
- integerg: number w/o decimals

car = 'BMW'
print "I love my", car
----------------------------------------------------
# ex05.py "More Variables and Printing"
- format strings
- %s: to put a value in a string
- %: provide a value after the string
- %d: for numbers ("digits")
- %r: for "raw data" (atually, "representation")

my_name = 'Islom Akhmedov'
print "My name is %s." % my_name

---------------------------------------------------
# ex06.py "Strings and Text"
- ': single quote
- ": double quote

age = 30
weight = 200
height = '5.11 inch tall'

print "I am %d years old, I weigh %d lbs and %s." % (age ,weight, height)

--------------------------------------------------
# ex07.py "More Printing"
- +: for joining the strings w/o spaces
- ,: for joining strings with spaces

a = 'Py'
b = 'thon'

print a + b

---------------------------------------------------
# ex08.py "Printing, Printing"
- True: Boolean value/keyword that does not need quotes
- False: Boolean value/keyword that does not need quotes

formatter = "%r %r"

print formatter % ('Super', 'man')

----------------------------------------------------
# ex09.py "Printing, Printing, Printing"
- \: backslash, used to escape characters
- \n: new line command
- """ """: triple quotes to set off several lines of text

days = "Mon\nTue\nWed\nThu\nFri\nSat\nSun"
print "Here are the days:", days


----------------------------------------------------
# ex10.py "What Was That?"
- \\: to escape a backslash \ within a string
- \': to escape a sing quote within a string
- \": to escape a doble quote within a string
- \r: carriage return within a string
- \t: tab within a string
- ''' ''': Alternative method of triple quotes

# The use of \ character encodes difficult to type charaters into a string.
print ' I am 6\'2" tall' # escape single-quote inside string, we could do the same for double-quotes.

# \n is used tof new line and \t is for tab character
print "\t This is cat food"


------------------------------------------------------
# ex11.py "Asking Questions" 
- raw_input: to get typed input from user

print "How old are you?"
age = raw_input(':?')
print age
# This is little advanced, but we can try x = int(raw_input()) which gets the number as string from raw_input() then converts it to an integer using int().


--------------------------------------------------------
# ex12.py "Prompting People"
- raw_input(*Prompt text: " Alternative way to put prompt in for raw_input from user
- pydoc: Shell command for information on Python topics
- pydoc topics: raw_input (ON Windows use python -m pydoc raw_input), open file, os, sys


-----------------------------------------------------
# ex13.py "Parameterd, Unpacking, Variables (I would also call it argument)"

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
# ex14.py  "Prompting and Passing"
from sys import argv

script, user_name = argv
promt = '> '

print "Hi %s, I am the %s script." % (user_name, script)
print "Do you like me %s" % user_name
likes = raw_input(promt)
print "You said %r" % likes

- prompt: A character that user can specify to ask for info from the user
-------------------------------------------------------
# ex15.py  "Reading Files"

- open: Make a file available to Python
- .: dot operator to join a function (or command or method) to an object
- .read: Read the content of the file
- .close: Close the file so it is not longer available to Python 
--------------------------------------------------------
# ex16.py "Reading and Write"
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
# ex17.py "More Files"
- os.path: a library that adapts the file/directory address to the specific requiments of  the operating system
- exists: a function to determine whether a specific files exists; yields a boolean True or False 

# print "Does the output file exist? %r" % exists(to_file)
# it will print True if the file exists.
--------------------------------------------------------
# ex18.py Names, Variables, Code, Functions
- def: to define custon functions
- (*args): to refer to list of arguments in a function (but better to just list the arguments next to the function name)
- : and intent: to set  block for function
----------------------------------------------------------
# ex19.py "Function and Variables"
- More info on  using variables within functions but no new terms or symbols
----------------------------------------------------------
# ex20.py "Functions and Files"
- .seek(): Go to specific position within a file (in bytes); .seak(0) - goes to the begining
- readline: read one line from a file 
- +=: shortcut for incrementing variable
--------------
# ex21.py "Functions Can Return Something"

- return: a valuew that a function makes available to use in a variable.



Reference link: https://www.youtube.com/watch?v=8nmekdC2r-c
























