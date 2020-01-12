import prompt
import random


def run(rounds_num, name):
    for i in range(rounds_num):
        question = random.randint(1, 100)
        print('Question: {}'.format(question))

        def is_prime(num):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        return 'no'
                return 'yes'
            return 'no'

        CORRECT_ANSWER = is_prime(question)
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
