print "Please, enter any number greater than 1 "
my_num = int(raw_input("> "))
i = 0
numbers = []

while i <= my_num:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i += 1 
	
	print  "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers:"

for num in numbers:
	print num

# in below example we are using while loop inside a function
# We need to convers "user_limit" to "int"
# raw_input() return value is str and state,ent is using var which is "int"
def numbers(limit):
	var = 0
	nums = []
	
	while var < limit:
		nums.append(var)
		var = var + 1
	print nums

user_limit = int(raw_input("Please give me a limit: "))
numbers(user_limit)
