"""
Implement a class that can convert a Python dictionary into an object.

    {
        'a': 1,
        'b': {
            'c': 2,
        },
    }

    obj.a    # should return 1
    obj.b.c  # should return 2

"""

class DictToObj(dict):
	def __init__(self, **entries):
		for key, value in entries.items():
			_value = (DictToObj(**value) if isinstance(value, dict) else value)
			self.__dict__[key] = _value
			