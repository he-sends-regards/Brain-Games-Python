import prompt
import random
from math import gcd


DESCRIPTION = 'Find greatest common divisor of two numbers'


def run():
    NUM1 = random.randint(0, 10)
    NUM2 = random.randint(0, 10)
    print('Question: {} {}'.format(NUM1, NUM2))

    USER_ANSWER = prompt.integer('Your answer: ')
    CORRECT_ANSWER = gcd(NUM1, NUM2)
    if USER_ANSWER == CORRECT_ANSWER:
        print('Correct!')
        return True
    else:
        result = '\"{}\" is wrong answer ;(. Correct answer was \"{}\"'
        print(result.format(USER_ANSWER, CORRECT_ANSWER))
        return False
