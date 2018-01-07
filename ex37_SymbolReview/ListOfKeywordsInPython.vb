						List of keywords in Python
Referenc Link:
https://www.programiz.com/python-programming/keyword-list#as

Keywords are the reserved words in Python. We cannot use a keyword as variable name, finction name or any other identifier.

Below is an example of the keywords belong to Python 2.7, they may get altered in different versions of Python. 
Some extra might get added or some might be removed. You can always get the list of keywords in you current 
version by typing the following in the prompt. 
------------------
$ python
Python 2.7.12 (default, Nov 20 2017, 18:23:56)
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import keyword
>>> print keyword.kwlist
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 
'try', 'while', 'with', 'yield']
-------------------

						Description of Keywords in Python with examples
True, False

True and False are truth values in Python. They are the results of comparison operations or logical (Boolean) operations 
in Python.

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

Here we can see that the first three statements are true so the interpreter returns True and returns False 
for the remaining three statements. True and False in Python is the same as 1 and 0. This can be justufied with 
following exmaple:
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

It is an object of its own datatype, the NoneType. We cannot create multiple "None" 
objects but we can assign it to variables. These variables will be equel to one another.

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

Void functions that do not return anything will return a "Nore" object automatically. 
"Nore" is alse returned by functions in which program flow does not enconter a return statement.
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

This program has a funtion that does not return a value, although it does some operations inside. 
So when we print (x), wee get "Nore" which  is returned automatically (implicitly).
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

Although this function has a return statement, it is not reached in every case. The function will ruturn True only when 
the input is even.

If we give the function an odd number, "Nore" is returned implicitly.


and, or, not

and, or, not are the logical operators in Python. and will result into True only if both the operands are True. 
The truth table for and is given below:

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

as is used to create an alias while importing a  module. It means giving a different name (user-defined) to a 
module while importing it.

As for example, Python has a standard module called math. Suppose we want to calculate what consine pi id using 
an alias. We can do it as follows using as:

-------------------------------
>>> import math as myAlias
>>> myAlias.cos(myAlias.pi)
-1.0
>>>
------------------------------

Here we imported the "math" module by giving the name myAlias. We can refer to the "math" module with this name. 
Using this name we calculated cos(pi) and we got -1.0 as the answer.


assert is used for debugging purposes.

While programming, sometime we wish to know the internal state or check if our assumptions are true. assert helps us 
to do this and find bugs more conveniently. assert is followrf by a condition.

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

"break" will end the smallest loop it is in and control flows to statement immediately below the loop. 
continue causes to the end the current  iteration of the loop, but not the whole loop.

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

Here, the for loop indends to print numbers from 1 to 10. But if condition is met when "i" is equal to 5 and 
we break from  the loop. Thus, only the range 1 to 4 is printed.
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

Here we use continue for the same program. So, when the condition is met, that iteration is skippet, 
but we do not exit the loop. Hence, all the values except 5 is printed out.


"class"

"class" is collection of related attributes and methods that try to represent a real world situation. 
This idea of putting data and function togather in a class is central tothe concept of object-oriented programming(OOP).

Classes can be defined anywhere in a program. But it is a good practice to define a single class in a module. 
Following is a simple udage:
---------------------------
class ExampleClass:
    def function1(parameters):
        …
    def function2(parameters):
        …
---------------------------


"def"

"def" is used to define a user-defined finction.

Function is a clock of related statements, which togather does some specific task. It helps us organize code 
into manageable chunks and also todo some repetitive task.

The usage to def is shown below:
--------------------------------
def function_name(parameters):
    …
------------------------------

"del"

"del" is used to delete the referece to an object. Evrything is object in Python. We can deletw a a variablw 
reference using "del"
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

if, else, elif are used to test some condition and execute block only if the condition is true, then 
we use if and elif. elif is short for else if. else is the block which is executed if the condition is false. 
This will be clear with the following example:
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
Here , the function checks the input number and prints the result if it is 1 or 2. Any input other than this 
will cause the else part of the code to execude.


except, raise, try

except, raise, try are used with exception in Python.

Exceptions are basically errors that suggests something went wrong while executing our program. IOError, 
ValueError, ZeroDevisionError, ImportError, NameError, TypeError etc. are few examples of exception in Python. 
"try...except" blocks are used to catch exceptions in Python.

We can raise an exception explicitly with the raise keyword. Following is an example:
------------------------------------
def reciprocal(num):
    try:
        r = 1/num #
    except:
        print('Exception caught')
        return
    return r

print(reciprocal(10))
print(reciprocal(0))
----------------------------------
Output:

0.1
Exception caught
None
-------------------------------------
note:  
------------------------------------
>>> 1 / 2            # Python 3 returns real quotient
0.5
>>> 1.0 / 2          # Python 2 returns real quotient
0.5
--------------------------------------

Here, the function "reciprocal" returns the reciprocal of the intup number.

When we enter 10, we get the normal out put of 0.1. But when we input 0, a ZeroDivisionError is reaised automatically.

THis is caught by our try...except block and we ruturn None. We could have also raised ZeroDivisionError 
explicitly the input and handled it elsewhere as folloows:
---------------------- 
if num == 0:
    raise ZeroDivisionError('cannot divide')
--------------------

'finally'

'finally' is used with try...except block to close up resources or file streams

Using 'finally' ensures that the block of code insight it gets executed even if there is an unhandles exception. 
For example:
-----------------------------
try:
    Try-block
except exception1:
    Exception1-block
except exception2:
    Exception2-block
else:
    Else-block
finally:
    Finally-block
-----------------------------
Here if there is an exception in the 'Try-block', it is handled in the except or less block.
But no matter in what order the execution flows, we can rest that the 'Finally-block' is executed
even if there is an error. THis is useful in cleaning up the resources.


for 

'for' is used for looping. Generally we use 'for' when we know the number of the times we want to loop
--------------------
names = ['John', 'Monica', 'Steven','Robin']
for i in names:
	print ('Hello' +i)
--------------------
Output:

Hello John
Hello Monica
Hello Steven
Hello Robin
--------------------
 
 from, import
 
 'import' keyword is used to import modules into current name space.
 from...import is used to import spcific attributes or functions into the current namespace.
 For example:
 -------------------------
 from math import cos
 -------------------------
 now we can use function simply as cos(), no need t write math.cos().
 
 global
 
 'global' is used to declare that a variable inside the function is global (outside the function).
 
 If we need to read the valuew of tha global variable, it is not necessary to define it as global.
 This is understood.
 
 If we we need to modify value of global variable inside a function, then we must declare it with global. Otherwise
  a local variable with the name is created.
  
  Following example will help us clarify this. 
---------------------------------
 globvar = 10
def read1():
    print(globvar)
def write1():
    global globvar
    globvar = 5
def write2():
    globvar = 15

read1()
write1()
read1()
write2()
read1()
-----------------------------------
Output:

10
5
5
--------------------------------------
Here, the read() function is just reading the value of globvar. So, we do not need to declare it as global.
But the write1() function is modifying the value, so we need to daclare it as global.
 
We can see in our output that the modification did take place (10 is changed to 5). The write2() also 
tries to modify this value. But we have not 
declared it as global.

Hence, a new local variable glovar is created which is not visible outside of this function.
Although we modify this variable to 15, the global variable remains unchanges. This is cleary visible in our output.

in

'in' is used to test if a sequence (list, tuple, string etc) contains a value. It return True if the value is 
present, else it returns False.
For example: 
 
----------------------------
>>> a = [1, 2, 3, 4, 5]
>>> 5 in a
True
>>> 10 in a
False
----------------------------

The secondary use of in is to traverse through a sequence in a for loop.
 
------------------------------
for i in 'hello':
    print(i)
------------------------------
Output:

h
e
l
l
o
-----------------------------

'is'

'is' is used in Python for testing object identity. While the == operatoris used to test if two variables 
are equal or not,
'is' is used to test if the two varibles refer to the same object.

It returns True if the objects are identical and Falseif not.
--------------------------------
>>> True is True
True
>>> False is False
True
>>> None is None
True
----------------------------------
We know that there is only one instance of True, False and None in Python, so they areidentical.
----------------------------------
>>> [] == []
True
>>> [] is []
False
>>> {} == {}
True
>>> {} is {}
False
-----------------------------------
An empty list or dictionary is equel to another empty one. But they are not identical
objects as they are located seperate in the memory. This is because list and dictionary are mutable (value can be changed).
-----------------------------------
>>> '' == ''
True
>>> '' is ''
True
>>> () == ()
True
>>> () is ()
True
--------------------------------------
Unlike the list and dictionary, string and tuple are immutable (value cannot be altered once defined).
Hence, two equal string or tulpe are identical as well. They refer to the same memory location.

'lambda'

'lambda' is used to create an anonimous finction (function with no name).
It is an inline function that does not contain a return statement. it consists of an expression that is 
eveluated and returned.
For example:

-----------------------------------------
a = lambda x: x*2
for i in range(1,6):
    print(a(i))
-----------------------------------------
Output:

2
4
6
8
10
-------------------------------------------
Here, we have created an inline function taht double the value, using the lambda statement.
We used this to double the values in a list containing 1 to 5.

'nonlocal'
 
The use of 'nonlocal' keyword is very much similar to globa; keyword. 'nonlocal' is used to declare 
that a variable inside a nested function (function inside a function) is used local to it,
meaning is lies in the outer inclosing function. If we need to modify the value of a nonlocal variable 
inside a nested function, we must declare it nonlocal.
Otherwise a local variable with that name is created inside nested function. 
Following example will help us to clarify this.
------------------------------------------
def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("Inner function: ",a)
    inner_function()
    print("Outer function: ",a)

outer_function()
-------------------------------------------
Output:

Inner function:  10
Outer function:  10
--------------------------------------------
Here, inner_function() is nested within the outer_function.

The varibale a in in the outer_function(). SO, if we want to modify it in the inner_function(),
we mut daclare it as nonlocal. Notice it is not global variable.

Hence, we see from the output that variable was successfully modified inside inner_function(). 
The result of nonlocal keyword as follows:
----------------------------------------------
def outer_function():
    a = 5
    def inner_function():
        a = 10
        print("Inner function: ",a)
    inner_function()
    print("Outer function: ",a)

outer_function()
----------------------------------------------
Output:

Inner function:  10
Outer function:  5
--------------------------------------------------
Here, we do not daclare that the variable a inside the nested function in nonlocal.
Hence, a new local variable with the same name is created, but the nonlocal a is not modofied as see in our output.

'pass'

'pass' is a null statement in Python. Nothing happens when it is executed. It is used as placeholder.

Suppose we have function that is not implemented yet, but we want to implement it in the future. Simple writing,
-------------------------------------------
def function(args):
-------------------------------------------- 
In the middle of a program will give us IndentationError. Instead of this, we cunstruct a balank body with the pass statement.
--------------------------------------------
def function(args):
    pass
---------------------------------------------
We can do the same thing in an empty class as well.
----------------------------------------------
class example:
    pass
-----------------------------------------------

'return'

'return' statement is used inside a function to exit it and return a value.

If  we do not return explicity, None is returned automatically. 
This is verified with following example.
------------------------------------------------
def func_return():
    a = 10
    return a

def no_return():
    a = 10

print(func_return())
print(no_return())
--------------------------------------------------
Output:

10
None
---------------------------------------------------

while 

while is used fro looping in Python.

The statements inside a while loop continue to execute intill condition for the while loop evelutes to 
False or a break statement is encountered.
Following program illustrates this.
-------------------------------------------------------
i = 5
while(i):
    print(i)
    i = i – 1
-------------------------------------------------------
Output:

5
4
3
2
1
-------------------------------------------------
Note that 0 is equal to False.

'with'

'with' statement is used to wrap the execution of a block of code within methods defined by the context manager.

Context manager is a class that implements __enter__ and __exit__ methods.
Use of with statement ensures that the __exit__ method is called at the end fo the nested block.
This concept is similar to the use of try...finally block. Here, is an example.
-----------------------------------------------------
with open('example.txt', 'w') as my_file:
    my_file.write('Hello world!')
--------------------------------------------------
This example writes the text 'Hello world!' to the file example.txt . File objects have __enter__
and __exit__ method defined within them, so the act as their own context manager.

First the __enter__ method is called, then the code within 'with' statement is executed and finally the __exit__ methon 
is called.
__exit__method is called even if there is an error. It basically closes the file stream.

'yeald'
 
'yield' is used inside a function like return statement. But yeald returns a generator.

Generator is an iterator that generates one item at a time. A large list of value will take up a lot of memory. 
Generators are useful in this situation as it generates only one value
at a time of storing all the values in memory.
For exmple:
------------------------------------------------------
>>> g = (2**x for x in range(100))
------------------------------------------------------
will create a generator g which generates powers of 2 up to the number two raised to the power 99. 
We can generate the numbers using the next() function as shown below.
-------------------------------------------------------
>>> next(g)
1
>>> next(g)
2
>>> next(g)
4
>>> next(g)
8
>>> next(g)
16
---------------------------------------------------------
And so on… This type of generator is returned by the yield statement from a function. Here is an example.
----------------------------------------------------------
def generator():
    for i in range(6):
        yield i*i

g = generator()
for i in g:
    print(i)
-----------------------
Output:

0
1
4
9
16
25
-----------------------------------------------------------------
Here, the function generator() returns a generator that generates square of numbers from 0 to 5. T
his is printed in the for loop.



Data Types

For data types, write out what makes up each one. For example, with strings write out how you create
a string. For numbers write out a few numbers.
---------------------------------------------------------------------------
Type 		Description 				Example					
---------------------------------------------------------------------------
True 		True boolean value. 			True or False == True	
---------------------------------------------------------------------------
False 		False boolean value. 			False and True == False	
---------------------------------------------------------------------------
None 		Represents ”nothing” or ”no value”. 	x = None				
---------------------------------------------------------------------------
strings		Stores textual information. 		i = ”hello”				
---------------------------------------------------------------------------
numbers		Stores integers. 			i = 100					
---------------------------------------------------------------------------
floats 		Stores decimals. 			i = 10.389					
----------------------------------------------------------------------------
lists 		Stores a list of things. 		j = [1,2,3,4]				
-----------------------------------------------------------------------------
dicts 		Stores a key=value mapping of things. 	e = {’x’: 1, ’y’: 2}		
-----------------------------------------------------------------------------


String Escape Sequences

Escape Description
\\ Backslash
\’ Single-quote
\” Double-quote
\a Bell
\b Backspace
\f Formfeed
\n Newline
\r Carriage
\t Tab
\v Vertical tab

String Formats
Same thing for string formats: use them in some strings to know what they do.

Escape Description Example
%d Decimal integers (not floating point). ”%d” % 45 == ’45’
%i Same as %d. ”%i” % 45 == ’45’
%o Octal number. ”%o” % 1000 == ’1750’
%u Unsigned decimal. ”%u” % -1000 == ’-1000’
%x Hexadecimal lowercase. ”%x” % 1000 == ’3e8’
%X Hexadecimal uppercase. ”%X” % 1000 == ’3E8’
%e Exponential notation, lowercase ’e’. ”%e” % 1000 == ’1.000000e+03’
%E Exponential notation, uppercase ’E’. ”%E” % 1000 == ’1.000000E+03’
%f Floating point real number. ”%f” % 10.34 == ’10.340000’
%F Same as %f. ”%F” % 10.34 == ’10.340000’
%g Either %f or %e, whichever is shorter. ”%g” % 10.34 == ’10.34’
%G Same as %g but uppercase. ”%G” % 10.34 == ’10.34’
%c Character format. ”%c” % 34 == ’”’
%r Repr format (debugging format). ”%r” % int == ”<type ’int’>”
%s String format. ”%s there” % ’hi’ == ’hi
there’
%% A percent sign.	”%g%%” % 10.34 == ’10.34%’

Operators

Some of these may be unfamiliar to you, but look them up anyway. Find out what they do, and if you
still can’t figure it out, save it for later.

Operator Description Example
+ Addition 2 + 4 == 6
- Subtraction 2 - 4 == -2
* Multiplication 2 * 4 == 8
** Power of 2 ** 4 == 16
/ Division 2 / 4.0 == 0.5
// Floor division 2 // 4.0 == 0.0
% String interpolate or modulus 2 % 4 == 2
< Less than 4 < 4 == False
> Greater than 4 > 4 == False
<= Less than equal 4 <= 4 == True
>= Greater than equal 4 >= 4 == True
== Equal 4 == 5 == False
!= Not equal 4 != 5 == True
<> Not equal 4 <> 5 == True
( ) Parenthesis len(’hi’) == 2
[ ] List brackets [1,3,4]
{ } Dict curly braces {’x’: 5, ’y’: 10}
@ At (decorators) @classmethod
, Comma range(0, 10)
: Colon def X():
. Dot self.x = 10
= Assign equal x = 10
; semi-colon print ”hi”; print ”there”
+= Add and assign x = 1; x += 2
-= Subtract and assign x = 1; x -= 2
*= Multiply and assign x = 1; x *= 2
/= Divide and assign x = 1; x /= 2
//= Floor divide and assign x = 1; x //= 2
%= Modulus assign x = 1; x %= 2
**= Power assign x = 1; x **= 2
