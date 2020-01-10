import prompt
import random


def run():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?\n')
    name = prompt.string('May I have your name? ')
    print('\nHello, {}!\n'.format(name))

    rounds_num = 3
    for i in range(rounds_num):
        def make_progression():
            result = []
            progression_limit = 9
            first_num = random.randint(0, 10)
            result.append(first_num)
            k = random.randint(1, 10)
            for i in range(progression_limit):
                result.append(result[i] + k)
            return result
        
        progression = make_progression()
        symbol_to_hide = progression[random.randint(0, 9)]
        question = progression.copy()
        question[question.index(symbol_to_hide)] = '..'
        print('Question: {}'.format(question))
        user_answer = prompt.integer('Your answer: ')
        if user_answer == symbol_to_hide:
            print('Correct!')
            continue
        else:
            result = '\"{}\" is wrong answer ;(. Correct answer was \"{}\"'
            print(result.format(user_answer, symbol_to_hide))
            return
    print('Congratulations, {}'.format(name))
    return
