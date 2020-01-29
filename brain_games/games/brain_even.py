import random


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def make_question():
    rand_num = random.randint(1, 100)
    print('Question: ' + str(rand_num))
    return correct_answer(rand_num)


def correct_answer(num):
    return 'yes' if num % 2 == 0 else 'no'
