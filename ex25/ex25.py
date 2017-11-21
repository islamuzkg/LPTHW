
# This is not a script, per se, but a module.
# That is, this document defines several functions
# that we can then use on other objects. The
# module will be called "ex25" (without the .py 
# extention). In addition, we are going to run 
# this from Python, and not the command line
# (i.e., UNIX Shell) that we used so far,
# In structions will be included at the bottom.

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping in off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
# Here are the iinstructions:
# reference Link: https://www.youtube.com/watch?v=sNmLKBsOjto

# 1. Start Python.
# python

# 2. Import this newly defined module.
# >>> ipmort ex25
# Note: Dom't type ".py" ou you'll get an error
# When you import it will create a new file on your
# computer called "ex25.pyc." which is "Python Bytecode Document."
# which helps the module load faster in the future. 
# You can, however, delete it if you want to

# 3. Create an object to work with.
# >>> sentence = "All good things come to those who wait."

# 4. Run "break_words" and show results
# >>> words = "ex25.break_words(sentence)"
# >>> words
# Note: You can also  print without  the intermidiate variable:
# >>> print ex25.break_words(sentence)

# 5. Run "sort_words" and show results
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words 

# 6. Run "print_first_word"(displays automatically)
# >>> ex25.print_first_word(words)

# 7. Run"print_last_word"(displays automatically)
# >>> ex25.print_last_word(words)

# 8. Run "sort_sentence" and show results
# >>> sorted_sentence = ex25.sort_sentence(sentence)
# >>> sorted_sentence
# Note: Zed used the object "sorted_words" for these
# but that might be mistake bc he used that earlier
# and all have variables so far use the function name, so 
# I'am calling the object "sorted_sentence."
# The output looks the same as "sorted_sentence." but used
# a different process to get there.

# 9. Run "print_first_and_last"(displays automatically)
# >>> ex25.print_first_and_last(sentence)

# 10. Run "print_first_and_last_sorted"(displays automatically)
# >>> ex25.print_first_and_last_sorted(sentence)

# If you type help(ex25) you'll see the first block of 
# text I wrote at the top and the text in triple quotes
# for each function below

# If you type help(ex25.break_words) you'll see just  
# the triple qoute text for that function. That's called
# a "documentation comment"

# Finally, you can avoid typing "ex25." at the beginning
# of everything if you import the module like this instead:
# >>>  from ex25 import * 
# Then  you can run the commands like this:

# >>> sentence = "All good things come to those who wait."
# >>> print break_words(sentece)

# to quite Python interpreter run command below:
# >>> quit()
