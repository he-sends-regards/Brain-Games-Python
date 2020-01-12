import prompt
import random
from math import gcd


def run(rounds_num, name):
    for i in range(rounds_num):
        NUM1 = random.randint(0, 10)
        NUM2 = random.randint(0, 10)
        print('Question: {} {}'.format(NUM1, NUM2))
        USER_ANSWER = prompt.integer('Your answer: ')
        CORRECT_ANSWER = gcd(NUM1, NUM2)
        if USER_ANSWER == CORRECT_ANSWER:
            print('Correct!')
            continue
        else:
            result = '\"{}\" is wrong answer ;(. Correct answer was \"{}\"'
            print(result.format(USER_ANSWER, CORRECT_ANSWER))
            return
    print('Congratulations, {}'.format(name))
    return
