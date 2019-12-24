"""
Implement a function that returns an inclusive list of numbers
from a Python slice style string with 1 <= N <= 10.

    '1'      # returns [1]
    ':7'     # returns [1, 2, 3, 4, 5, 6, 7]
    '8:'     # returns [8, 9, 10]
    '2:5'    # returns [2, 3, 4, 5]
    'a:b'    # returns 'Range values must be integers!'
    '1:2:3'  # returns 'Only two values allowed!'

"""

def range_parser(s):
	if len(s) == 1 and isinstance(s[0],str):
		return [int(s[0])]

	first_digit = s[0]

	if len(s) == 2 and first_digit != ":":
		return list(range(int(first_digit),11))

	if len(s) == 2 and first_digit == ":":
		return list(range(1,int(s[1])+1))

	if len(s) > 3:
		return "Only two values allowed!"

	if  len(s) == 3 and s[0].isalpha():
		return "Range values must be integers!"

	if len(s) == 3:
		return list(range(int(s[0]),int(s[2])+1))