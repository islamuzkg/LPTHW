# https://stackoverflow.com/questions/47137880/difference-between-inheritance-and-composition-in-a-mvc-architecture
# https://www.cs.uct.ac.za/mit_notes/python/Classes.html
class Person:

    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, name, surname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." % title)

        self.title = title
        self.name = name
        self.surname = surname

person = Person("Mr" ,"Doe", "John")
print ">>> This output is from Person"
print person.title

class Person1:
    deceased = False

    def mark_as_deceased(self):
        self.deceseased = True
        return self.deceased

person1 = Person1()
print ">>>>>>>>> This output is from Person1"
print person1.mark_as_deceased()


class Person2:

    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

jane = Person2()
bob = Person2()

jane.add_pet("cat")
print ">>>>>>>> This output is from Person2"
print jane.pets
print bob.pets

class Smith:
    surname = "Smith"
    profession = "smith"

    def __init__(self, name, profession=None):
        self.name = name
        if profession is not None:
            self.profession = profession

person = Smith('Alen')

print ">>>>>>>>> This output is from Smith"
print person.name # name is instance attribute
print person.surname # surname is class attribute
print person.profession




class Person3:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self): #instance method
         # instance object accessible through self
         return "%s %s" % (self.name, self.surname)

    @classmethod
    def allowed_titles_starting_with(cls, startswith): #class method
        # class or instance object acccessible through cls
        return [t for t in cls.TITLES if t.startswith(startswith)]

    @staticmethod
    def allowed_titles_ending_with(endswith):   #static method
        # no parameter for class or instance object
        # we have to use Person3 directly
        return [t for t in Person3.TITLES if t.endswith(endswith)]

jane = Person3("Jane", "Smith")

print ">>>>>>>>>>>>>>> Below output is from Person3"
print jane.fullname()

print ">>>>>>> Person3 classic method"
print jane.allowed_titles_starting_with("M")
print Person3.allowed_titles_starting_with("M")

print ">>>>>>> Person3 static method"
print jane.allowed_titles_ending_with("s")
print Person3.allowed_titles_ending_with("s")


class Numbers:
    MULTIPLIER = 8.9

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def multiply(cls, a):
        return cls.MULTIPLIER * a

    @staticmethod
    def substract(b, c):
        return b -c

    @property
    def value(self):
        return (self.x - self.y)

    @value.setter
    def value(self, xy_tuple):
        self.x, self.y = xy_tuple

    @value.deleter
    def value(self):
        del self.x
        del self.y




num = Numbers(4, 5)

print ">>>>>>>>>> Below is output from Math"
print num.add()
print num.multiply(5)
print num.substract(5, 3)
print ">>>>>>>>>>>>>>>>"
print num.value
