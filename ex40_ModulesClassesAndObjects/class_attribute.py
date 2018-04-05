# https://stackoverflow.com/questions/47137880/difference-between-inheritance-and-composition-in-a-mvc-architecture

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
print ">>> This output is from Person1"
print person1.mark_as_deceased()


class Person2:

    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

jane = Person2()
bob = Person2()

jane.add_pet("cat")
print ">>> This output is from Person2"
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

print ">>> This output is from Smith"
print person.name # name is instance attribute
print person.surname # surname is class attribute
print person.profession
