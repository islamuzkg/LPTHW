# Reference Link: http://sthurlow.com/python/lesson06/

list = [1, 2, 3]
dictionary = {3: "three", 1: "one", 2: "2"}
tuple = (1, 2, 3)
set = {1, 2, 3}
'''
for i in list:
	print "list: %d" % i

for i in dictionary:
	print "this is %s" % i

for i in tuple:
	print("tuple: %d" % i)

for i in set:
	print("set: %d" % i)
'''

# this is tuples
months = ('January','February','March','April','May','June',\
'July','August','September','October','November','December')

print "I am just testing months:", months[0]

print "--------------------------"
for i in range(12):
	print months[i]
print "---------------------------"

# this is list
cats = ['Tom', 'Snappy', 'Kitty', 'Jessie', 'Chester']
print "My cats name is:", cats[4]

# we are using append function to add another new value to the list
cats.append("Chathy")
print "testing after appending:", cats[5]

# we can also recall a range of examples, like below
print cats[0:3]

for i in cats[0:3]:
	print i

# Remove your 2nd cat, Sanppy. Woe is you.
print cats
del cats[1]
print cats


# creating dictionary reference link :http://sthurlow.com/python/lesson06/
# Make phone boook

phonebook = {'Andrew Parson':88006336,'Emily Everett':6784346, 'Peter Power':7658344, 'Lewis Lame':1122345}
'''
# You can also write it as below
phonebook = {'Andrew Parson':88006336, \
'Emily Everett':6784346, 'Peter Power':7658344, \
'Lewis Lame':1122345}
'''
print phonebook['Andrew Parson']

# Adding entries to a phonebook
phonebook['Gingerbread Man'] = 1234567

print phonebook
del phonebook['Andrew Parson']
print phonebook
