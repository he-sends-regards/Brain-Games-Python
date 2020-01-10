import prompt
import random


def run():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?\n')
    name = prompt.string('May I have your name? ')
    print('\nHello, {}!\n'.format(name))

    rounds_num = 3
    for i in range(rounds_num):
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        operations = {
            'sum': '{} + {}'.format(num1, num2),
            'diff': '{} - {}'.format(num1, num2),
            'mult': '{} * {}'.format(num1, num2),
        }
        operation_index = random.randint(1, 4)

        def choose_operation(index):
            if index == 1:
                print('Question: ' + operations['sum'])
                return 'sum'
            elif index == 2:
                print('Question: ' + operations['diff'])
                return 'diff'
            print('Question: ' + operations['mult'])
            return 'mult'

        operation = choose_operation(operation_index)

        def find_answer(operation_name):
            if operation_name == 'sum':
                return num1 + num2
            elif operation_name == 'diff':
                return num1 - num2
            return num1 * num2

        correct_answer = find_answer(operation)
        user_answer = prompt.integer('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            continue
        else:
            result = '\"{}\" is wrong answer ;(. Correct answer was \"{}\"'
            print(result.format(user_answer, correct_answer))
            return
    print('Congratulations, {}'.format(name))
    return
