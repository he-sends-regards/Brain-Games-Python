import random


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def make_question():
    rand_num = random.randint(1, 100)
    return str(rand_num), 'yes' if is_even(rand_num) else 'no'


def is_even(num):
    return num % 2 == 0
