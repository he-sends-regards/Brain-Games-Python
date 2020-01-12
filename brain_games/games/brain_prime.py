import prompt
import random
from math import sqrt, ceil


def run(rounds_num, name):
    for i in range(rounds_num):
        question = random.randint(1, 100)
        print('Question: {}'.format(question))

        def is_prime_check(num):
            LIMIT_PRIME_CHECK = ceil(sqrt(num))
            print(LIMIT_PRIME_CHECK)
            for i in range(2, LIMIT_PRIME_CHECK):
                if (num % i) == 0:
                    return 'no'
            return 'yes'

        CORRECT_ANSWER = is_prime_check(question)
        USER_ANSWER = prompt.string('Your answer: ')
        if USER_ANSWER == CORRECT_ANSWER:
            print('Correct!')
            continue
        else:
            result = '\"{}\" is wrong answer ;(. Correct answer was \"{}\"'
            print(result.format(USER_ANSWER, CORRECT_ANSWER))
            return
    print('Congratulations, {}'.format(name))
    return
