import prompt
import random
from math import gcd


def run(rounds_num, name):
    for i in range(rounds_num):
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        print('Question: {} {}'.format(num1, num2))
        user_answer = prompt.integer('Your answer: ')
        correct_answer = gcd(num1, num2)
        if user_answer == correct_answer:
            print('Correct!')
            continue
        else:
            result = '\"{}\" is wrong answer ;(. Correct answer was \"{}\"'
            print(result.format(user_answer, correct_answer))
            return
    print('Congratulations, {}'.format(name))
    return
