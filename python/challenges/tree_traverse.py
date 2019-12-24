"""
Given a deeply nested dict, create a function that returns a
value within a tree when given the tree and a key. If there are
duplicates, the first result found should be returned.

    {
        'a': {
            'b': 123,
            'c': 456,
            'd': {
                'z': 789,
            },
        },
        'x': {
            'y': 111,
        },
    }  # input of 'z' should return '789'

"""

def tree_traverse(tree, key):
    for k, v  in tree.items():
        if k == key:
            return v
        elif isinstance(v, dict):
            found = tree_traverse(v, key) 
            if found is not None:
                return found