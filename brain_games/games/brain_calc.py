import prompt
import random


def run(rounds_num, name):
    for i in range(rounds_num):
        NUM1 = random.randint(0, 10)
        NUM2 = random.randint(0, 10)
        operations = {
            'sum': '{} + {}'.format(NUM1, NUM2),
            'diff': '{} - {}'.format(NUM1, NUM2),
            'mult': '{} * {}'.format(NUM1, NUM2),
        }
        OPERATION_INDEX = random.randint(1, 4)

        def choose_operation(index):
            if index == 1:
                print('Question: ' + operations['sum'])
                return 'sum'
            elif index == 2:
                print('Question: ' + operations['diff'])
                return 'diff'
            print('Question: ' + operations['mult'])
            return 'mult'

        operation = choose_operation(OPERATION_INDEX)

        def find_answer(operation_name):
            if operation_name == 'sum':
                return NUM1 + NUM2
            elif operation_name == 'diff':
                return NUM1 - NUM2
            return NUM1 * NUM2

        CORRECT_ANSWER = find_answer(operation)
        USER_ANSWER = prompt.integer('Your answer: ')
        if USER_ANSWER == CORRECT_ANSWER:
            print('Correct!')
            continue
        else:
            result = '\"{}\" is wrong answer ;(. Correct answer was \"{}\"'
            print(result.format(USER_ANSWER, CORRECT_ANSWER))
            return
    print('Congratulations, {}'.format(name))
    return
