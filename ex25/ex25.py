
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
		
