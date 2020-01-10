import prompt
import random


def run(rounds_num, name):
    for i in range(rounds_num):
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
