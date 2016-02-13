from random import random, uniform


def generate_list(size=100, bound=1000, negatives=False, nearly_sorted=False):
    """Create a list of randomly generated integes.

    Args:
        size (Int): The size of the list.
        bound (Int): The maximum value of integers in the list.

    Return:
        [Int]: A random list of integers.

    TODO:
        Add ability to make nearly sorted list
    """
    if negatives:
        return [int(bound*uniform(-1, 1)) for i in xrange(size)]
    return [int(bound*random()) for i in xrange(size)]
