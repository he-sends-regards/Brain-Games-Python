import prompt
import random
from math import sqrt, ceil


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def make_question():
    rand_num = random.randint(1, 100)
    print('Question: ' + str(rand_num))
    return correct_answer(rand_num)


def correct_answer(num):
    lim = ceil(sqrt(num))
    for i in range(2, lim):
        if (num % i) == 0:
            return 'no'
    return 'yes'
