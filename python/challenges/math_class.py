"""
Implement a math class with methods for addition, subtraction,
multiplication and division. If an input is provided that is not an
int, a message should be returned instead of raising an error.

    'a' + 3  # should return 'Inputs must be numbers!'

"""

class Math:
	def add(self,x,y):
		if not isinstance(x, int) or not isinstance(y, int):
			return 'Inputs must be numbers!'
		return x + y

	def subtract(self,x,y):
		if not isinstance(x, int) or not isinstance(y, int):
			return 'Inputs must be numbers!'
		return x - y

	def multiply(self,x,y):
		if not isinstance(x, int) or not isinstance(y, int):
			return 'Inputs must be numbers!'
		return x * y	

	def divide(self,x,y):
		if not isinstance(x, int) or not isinstance(y, int):
			return 'Inputs must be numbers!'
		return x / y