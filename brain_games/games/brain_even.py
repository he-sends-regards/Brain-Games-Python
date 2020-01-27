import prompt
import random


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def run():
    NUM = random.randint(1, 100)
    print('\nQuestion: {}'.format(NUM))

    CORRECT_ANSWER = 'yes' if NUM % 2 == 0 else 'no'
    ANSWER = prompt.string('Your answer: ')
    if CORRECT_ANSWER == ANSWER:
        print('Correct!')
        return True
    else:
        result = '\n\"{}\" is wrong answer ;(. Correct answer was \"{}\"'
        print(result.format(ANSWER, CORRECT_ANSWER))
        return False
