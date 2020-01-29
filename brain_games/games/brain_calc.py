import random


DESCRIPTION = 'What is the result of the expression?'


def make_question():
    num_1 = random.randint(0, 10)
    num_2 = random.randint(0, 10)
    operations = {
        'sum': '{} + {}'.format(num_1, num_2),
        'diff': '{} - {}'.format(num_1, num_2),
        'mult': '{} * {}'.format(num_1, num_2),
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
    return correct_answer(num_1, num_2, operation)


def correct_answer(num_1, num_2, operation_name):
    if operation_name == 'sum':
        return str(num_1 + num_2)
    elif operation_name == 'diff':
        return str(num_1 - num_2)
    return str(num_1 * num_2)
