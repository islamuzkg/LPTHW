# The 4 Major Ways to Do String Formatting in Python
# https://dbader.org/blog/python-string-formatting

>>> errno = 50159747054
>>> name = 'Bob'

WE want to print below line
'Hey Bob, there is a 0xbadcoffee error'

#1 - "Old Style" String Fromatting (%-operator)
>>> 'Hello, %s' % name
'Hello, Bob'
>>> 
>>> '%x' % errno
'badc0ffee'

>>> 'Hey %s, there is a 0x%x error!' % (name, errno)
'Hey Bob, there is a 0xbadc0ffee error!'
>>> 
>>>
>>> 'Hey %(name)s, there is a 0x%(errno)x error!' % {"name": name, "errno": errno}
'Hey Bob, there is a 0xbadc0ffee error!'
>>> 

------------------------------------------------------
#2 - "New Style" String Formating (string.format)

>>> 'Hello, {}'.format(name)
'Hello, Bob'
>>> 
>>> 
>>> 'Hey  {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errno)
'Hey  Bob, there is a 0xbadc0ffee error!'
>>> 

--------------------------------------------------------
#3 - Literal String Interpolation (Python 3.6+)

>>> f'Hello, {name}!'
'Hello, Bob!'
>>> 
>>> 
>>> a = 5
>>> b = 10
>>>
>>> f'Five plus ten is {a + b} and not {2 * (a + b)}'
'Five plus ten is 15 and not 30'
>>> 
>>>
>>> def greet(name, question):
...     return f"Hello, {name}! How's it {question}?"
... 
>>> greet('Bob', 'going')
"Hello, Bob! How's it going?"
>>> 
>>> 
>>>
### Below function gives same output
>>> def greet(name, question):
...     return "Hello, " + name + "! How's it" + question + "?"
... 
>>> greet('Bob', 'going')
"Hello, Bob! How's itgoing?"
>>> 

---------------------------------------------------------
#4 - Template Strings (Standar Library)
>>> from string import Template
>>> t = Template("Hey, $name!")
>>> t.substitute(name=name)
'Hey, Bob!'
>>> 
>>>
>>> templ_string = 'Hey $name, there is a $error error!'
>>> Template(templ_string).substitute(name=name, error=hex(errno))
'Hey Bob, there is a 0xbadc0ffee error!'
>>> 
>>>
>>>
>>> class Error:
...     def __init__(self):
...             pass
... 
>>> err = Error()
>>> user_input = '{error.__init__.__globals__[SECRET]}'
>>> user_input.format(error=err)
'this-is-a-secret'
>>> 


