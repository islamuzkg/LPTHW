"""
One line if statement in Python (ternary conditional operator)
Reference Link: https://www.pythoncentral.io/one-line-if-statement-in-python-ternary-conditional-operator/

Basic if statement (ternary operator) info

Many programming languages have a ternary operator, which define a conditional expression. The most common usage is to make a terse simple conditional assignment statement. In other words, it offers one-line code to evaluate the first expression if the condition is true, otherwise it evaluates the second expression. 
Programming languages derived from C usually have following syntax:


 <condition> ? <expression1> : <expression2>


The Python BDFL (creator of Python, Guido van Rossum) rejected it as non-Pythonic, since it is hard to understand for people not used to C. Moreover, the colon already has many uses in Python. So, when PEP 308 was approved, Python finally received its own shortcut conditional expression:

 <expression1> if <condition> else <expression2>

It first evaluates the condition; if it returns True, expression1 will be evaluated to give the result, otherwise expression2. Evaluation is lazy, so only one expression will be executed.
let's take a look at this example:
"""
"""
>>> age = 15
>>> # Conditions are evaluated from left to right
>>> print('kid' if age < 18 else 'adult')
kid
"""

choice = "2"; print("wowo"  if "0" in choice or "1" in choice else "hmm")
