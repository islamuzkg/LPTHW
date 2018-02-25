# Instance, Class, and Static Methods
# Reference LInk: https://realpython.com/blog/python/instance-class-and-static-methods-demystified/
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

