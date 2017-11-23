from sys import argv

script, filename = argv

some_file = open(filename)
print some_file.read()
some_file.close()

same_file = open("ex16-sd2.py")
print same_file.read()
same_file.close()
