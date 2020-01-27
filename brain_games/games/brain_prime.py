import prompt
import random
from math import sqrt, ceil


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def run():
    question = random.randint(1, 100)
    print('Question: {}'.format(question))

    def is_prime_check(num):
        LIMIT_PRIME_CHECK = ceil(sqrt(num)) + 1
        for i in range(2, LIMIT_PRIME_CHECK):
            if (num % i) == 0:
                return 'no'
        return 'yes'

    CORRECT_ANSWER = is_prime_check(question)
    USER_ANSWER = prompt.string('Your answer: ')
    if USER_ANSWER == CORRECT_ANSWER:
        print('Correct!')
        return True
    else:
        result = '\"{}\" is wrong answer ;(. Correct answer was \"{}\"'
        print(result.format(USER_ANSWER, CORRECT_ANSWER))
        return False
