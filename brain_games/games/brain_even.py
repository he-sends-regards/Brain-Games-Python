import prompt
import random


def run(rounds_num, name):
    for i in range(rounds_num):
        NUM = random.randint(1, 100)
        print('\nQuestion: {}'.format(NUM))
        CORRECT_ANSWER = 'yes' if NUM % 2 == 0 else 'no'
        ANSWER = prompt.string('Your answer: ')
        if CORRECT_ANSWER == ANSWER:
            print('Correct!')
        else:
            result = '\n\"{}\" is wrong answer ;(. Correct answer was \"{}\"'
            print(result.format(ANSWER, CORRECT_ANSWER))
            print('Let\'s try again, {}'.format(name))
            return
    print('\nCongratulations, {}'.format(name))
    return
