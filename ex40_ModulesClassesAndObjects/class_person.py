# Reference Link: http://python-textbok.readthedocs.io/en/1.0/Classes.html#defining-and-using-a-class
import datetime	# we will use this for date objects

class Person:

    def __init__(self, name, surname, birthday, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthday = birthday

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthday.year

        print ">>>>>>> We are chekcing the year 1st:", today.year # for testing
        print "<<<<<< And birthday year is: ", self.birthday.year
        print today

        if today  < datetime.date(today.year, self.birthday.month, self.birthday.day):
            age -= 1

        return age



person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 9709",
    "jane.doe@example.com"
)

print person.name # python2 way of printing
print(person.email) # python3 way of printing
print person.age()
