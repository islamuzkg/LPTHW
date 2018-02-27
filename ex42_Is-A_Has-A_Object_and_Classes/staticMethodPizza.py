# https://dbader.org/blog/python-string-formatting
#https://realpython.com/blog/python/instance-class-and-static-methods-demystified/
import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')


    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circl_area(r):
        return r ** 2 * math.pi
