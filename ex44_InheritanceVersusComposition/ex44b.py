class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent):

    def override(self):
        print ">> This was a Child class"
        print "CHILD override()"
        print "<<This was a Child class"

dad = Parent()
son = Child()

dad.override()
son.override()
