import random
from math import sqrt, ceil


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def make_question():
    rand_num = random.randint(1, 100)
    return str(rand_num), 'yes' if is_prime(rand_num) else 'no'


def is_prime(num):
    lim = ceil(sqrt(num))
    for i in range(2, lim):
        if (num % i) == 0:
            return False
    return True
