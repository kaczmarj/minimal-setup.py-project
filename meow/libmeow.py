import random


def get_random_meow():
    """Return a string meow with a random number of e's and o's.

    Examples are meeooow and meeoooow.
    """
    return "m" + "e" * random.randint(2, 7) + "o" * random.randint(2, 7) + "w"
