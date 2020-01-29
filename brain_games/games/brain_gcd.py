import random
from math import gcd


DESCRIPTION = 'Find greatest common divisor of two numbers'


def make_question():
    num_1 = random.randint(0, 10)
    num_2 = random.randint(0, 10)
    print('Question: {} {}'.format(num_1, num_2))
    return correct_answer(num_1, num_2)


def correct_answer(num_1, num_2):
    return str(gcd(num_1, num_2))
