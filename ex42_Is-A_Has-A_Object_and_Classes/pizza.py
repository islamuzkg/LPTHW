# Instance, Class, and Static Methods
# Reference LInk: https://realpython.com/blog/python/instance-class-and-static-methods-demystified/
class Pizza:
	def __init__(self, ingredients):
		self.ingredients = ingredients
	
	def __repr__(self):
		return f'Pizza({self.ingredients!r})'
	# On Python 2 and versions of Python 
	# 3 before 3.6 you’d use a different string formatting expression
	# for example:
	# def __repr__(self):
    # return 'Pizza(%r)' % self.ingredients

	@classmethod
	def mergherita(cls):
		return cls(['mozzarella', 'tomatoes'])
	
	@classmethod
	def prosciutto(cls):
		return cls(['mozzarella', 'tomatoes', 'ham'])
