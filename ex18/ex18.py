# This one is like scrpits with argv

def two_arguments(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def two_again_arguments(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def one_argument(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def no_argument():
	print "I got nothin'."
two_arguments("Zed", "Shaw")
two_again_arguments("Zed", "Shaw")
one_argument("Firtst!")
no_argument()
two_arguments("I am islom Akhmedov", "How about you?")
two_again_arguments("", "")
