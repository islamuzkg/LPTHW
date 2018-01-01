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

























