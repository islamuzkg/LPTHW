						List of keywords in Python
Referenc Link:
https://www.programiz.com/python-programming/keyword-list#as

Keywords are the reserved words in Python. We cannot use a keyword as variable name, finction name or any other identifier.

Below is an example of the keywords belong to Python 2.7, they may get altered in different versions of Python. Some extra might get added or some might be removed. You can always get the list of keywords in you current version by typing the following in the prompt. 
------------------
$ python
Python 2.7.12 (default, Nov 20 2017, 18:23:56)
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import keyword
>>> print keyword.kwlist
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
-------------------

						Description of Keywords in Python with examples
True, False

True and False are truth values in Python. They are the results of comparison operations or logical (Boolean) operations in Python.

For example:
---------------------
>>> 1 == 1
True
>>> 5 > 3
True
>>> 5 == 3
False
>>> 10 <= 1
False
>>> True and False
False
>>>
-------------------

Here we can see that the first three statements are true so the interpreter returns True and returns False for the remaining three statements. True and False in Python is the same as 1 and 0. This can be justufied with following exmaple:
---------------------
>>> True == 1
True
>>> True == 0
False
>>> False == 1
False
>>> False == 0
True
>>> True + True
2
>>>
--------------------


None

"None" is a special constant in Python that represents the absence of a value or a null value.

It is an object of its own datatype, the NoneType. We cannot create multiple "None" objects but we can assign it to variables. These variables will be equel to one another.

We must take special care of "Nore" does not imply  False, 0 any empty list, dictionary, string etc.
For exmaple:
--------------------
>>> None == 0
False
>>> None == []
False
>>> None == False
False
>>> x = None
>>> y = None
>>> y == x
True
>>>
---------------------

Void functions that do not return anything will return a "Nore" object automatically. "Nore" is alse returned by functions in which program flow does not enconter a return statement.
For example:
----------------------
def a_void_function():
    a = 1
    b = 2
    c = a + b

x = a_void_function()
print(x)
--------------------
Output:

None
-----------------------

This program has a funtion that does not return a value, although it does some operations inside. So when we print (x), wee get "Nore" which  is returned automatically (implicitly).
Similarly, below is another example:

-----------------------
def improper_return_function(a):
    if (a % 2) == 0:
        return True

x = improper_return_function(3)
print(x)
---------------------
Output:

None
-----------------------

Although this function has a return statement, it is not reached in every case. The function will ruturn True only when the input is even.

If we give the function an odd number, "Nore" is returned implicitly.


and, or, not

and, or, not are the logical operators in Python. and will result into True only if both the operands are True. The truth table for and is given below:

+-----------------+---------------+
|AND              |True?          |
+-----------------+---------------+
|True and False   |False          |
+-----------------+---------------+
|True and True    |True           |
+-----------------+---------------+
|False and True   |False          |
+-----------------+---------------+
|False and False  |False          |
+-----------------+---------------+

or will result True if any of the operands is True. The truth table for or is given below: 

+----------------+---------------+
|OR              |True?          |
+----------------+---------------+
|True or False   |True           |
+----------------+---------------+
|True or True    |True           |
+----------------+---------------+
|False or True   |True           |
+----------------+---------------+
|False or False  |False          |
+----------------+---------------+

not operator is used to invert the truth value. The truth table for not is given below:

+---------------+---------------+
|NOT		|True?		|
+-------------------------------+
|not False	|True		|
+---------------+---------------+
|not True	|False		|
+---------------+---------------+


as

as is used to create an alias while importing a  module. It means giving a different name (user-defined) to a module while importing it.

As for example, Python has a standard module called math. Suppose we want to calculate what consine pi id using an alias. We can do it as follows using as:

-------------------------------
>>> import math as myAlias
>>> myAlias.cos(myAlias.pi)
-1.0
>>>
------------------------------

Here we imported the "math" module by giving the name myAlias. We can refer to the "math" module with this name. Using this name we calculated cos(pi) and we got -1.0 as the answer.


assert is used for debugging purposes.

While programming, sometime we wish to know the internal state or check if our assumptions are true. assert helps us to do this and find bugs more conveniently. assert is followrf by a condition.

If the condiiton is true, nothing happens. But if the condition is false, AssertionError is raised.
For example: 
------------------------------
>>> a = 4
>>> assert a < 5
>>> assert a > 5, "The value of a is too small"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: The value of a is too small
----------------------------

For our better understanding, we can also provide a message to be printed with the AsserionError.


At this point we can note that,

assert condition, message

is equivalent to,

if not condition:
    raise AssertionError(message)

break, continue

"break" and "continue" are used inside for and while loops to alter their normal behavior.

"break" will end the smallest loop it is in and control flows to statement immediately below the loop. continue causes to the end the current  iteration of the loop, but not the whole loop.

This can be illustrated with the following two exampmles:
------------------------
for i in range(1,11):
	if i == 5:
		break
	print (i)
------------------------
Output:

1
2
3
4
------------------------

Here, the for loop indends to print numbers from 1 to 10. But if condition is met when "i" is equal to 5 and we break from  the loop. Thus, only the range 1 to 4 is printed.
------------------------
for i in range(1,11):
    if i == 5:
        continue
    print(i)
-----------------------
Output:

1
2
3
4
6
7
8
9
10
-----------------------------

Here we use continue for the same program. So, when the condition is met, that iteration is skippet, but we do not exit the loop. Hence, all the values except 5 is printed out.


"class"

"class" is collection of related attributes and methods that try to represent a real world situation. This idea of putting data and function togather in a class is central tothe concept of object-oriented programming(OOP).

Classes can be defined anywhere in a program. But it is a good practice to define a single class in a module. Following is a simple udage:
---------------------------
class ExampleClass:
    def function1(parameters):
        …
    def function2(parameters):
        …
---------------------------


"def"

"def" is used to define a user-defined finction.

Function is a clock of related statements, which togather does some specific task. It helps us organize code into manageable chunks and also todo some repetitive task.

The usage to def is shown below:
--------------------------------
def function_name(parameters):
    …
------------------------------

"del"

"del" is used to delete the referece to an object. Evrything is object in Python. We can deletw a a variablw reference using "del"
------------------------
>>> a = b = 5
>>> del a
>>> a
Traceback (most recent call last):
  File "<string>", line 301, in runcode
  File "<interactive input>", line 1, in <module>
NameError: name 'a' is not defined
>>> b
5
-------------------------

Here we can see that the reference of the variable "a" was deleted. So, it is no longer defined. But "b" still exists.

"del" is also used to delete items from a list o a dictionary:
-------------------------
>>> a = ['x','y','z']
>>> del a[1]
>>> a
['x', 'z']
--------------------------

if, else, elif 

if, else, elif are used to test some condition and execute block only if the condition is true, then we use if and elif. elif is short for else if. else is the block which is executed if the condition is false. This will be clear with the following example:
-------------------------------
def if_example(a):
    if a == 1:
        print('One')
    elif a == 2:
        print('Two')
    else:
        print('Something else')

if_example(2)
if_example(4)
if_example(1)
-----------------------------
Output:

Two
Something else
One
-----------------------------
Here , the function checks the input number and prints the result if it is 1 or 2. Any input other than this will cause the else part of the code to execude.


except, raise, try

except, raise, try are used with exception in Python.

Exceptions are basically errors that suggests something went wrong while executing our program. IOError, ValueError, ZeroDevisionError, ImportError, NameError, TypeError etc. are few examples of exception in Python. "try...except" blocks are used to catch exceptions in Python.

We can raise an exception explicitly with the raise keyword. Following is an example:
