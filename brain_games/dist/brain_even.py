import prompt
import random


def run():
    print('Answer "yes" if number even otherwise answer "no".\n')
    name = prompt.string('May I have your name? ')
    print('\nHello, {}!'.format(name))

    for i in range(3):
        num = random.randint(1, 100)
        print('\nQuestion: {}'.format(num))
        correct_answer = 'yes' if num % 2 == 0 else 'no'
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            print('Correct!')
        else:
            result = '\n\"{}\" is wrong answer ;(. Correct answer was \"{}\"'
            print(result.format(answer, correct_answer))
            print('Let\'s try again, {}'.format(name))
            return
    print('\nCongratulations, {}'.format(name))
    return
