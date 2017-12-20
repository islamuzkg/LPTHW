def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def substract(a, b):
	print "SUBSTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DEVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"


age = add(25, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
ages = add(40, 50)
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "\nHe is a pzzle.\n"

what = add(age, substract(height, multiply(weight, divide(iq,2))))
print add(age, substract(height, multiply(weight, divide(iq,2))))


print "That becomes: ", what, "Can you do it hy hand?\n"
blah = add(40, 20)
bleen = substract(70, 80)



def isequal(a, b):
    print "Is %r equal to %r? - " % (a, b) ,
    return (a == b)

print isequal(50, 40)


what_again = divide(age, divide(weight, add(age, substract(height,2))))
print divide(age, divide(weight, add(age, substract(height, 2))))

print "here is ", what_again
