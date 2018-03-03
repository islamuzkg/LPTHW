# http://effbot.org/pyfaq/tutor-whats-the-difference-between-import-foo-and-from-foo-import.htm
#https://realpython.com/blog/python/instance-class-and-static-methods-demystified/
import math
class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')


    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

"""
>>> import staticMethodPizza
>>> s = staticMethodPizza
>>> p = s.Pizza(4, ['mazzarella', 'tomatoes'])
>>> p
Pizza(4, ['mazzarella', 'tomatoes'])
>>> p.area()
"""
