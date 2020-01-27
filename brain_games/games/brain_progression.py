import prompt
import random


DESCRIPTION = 'Find missed element of the progression'


def run():
    def make_progression():
        result = []
        PROGRESSION_LIMIT = 9
        FIRST_NUM = random.randint(0, 10)
        result.append(FIRST_NUM)
        K = random.randint(1, 10)
        for i in range(PROGRESSION_LIMIT):
            result.append(result[i] + K)
        return result

    PROGRESSION = make_progression()
    SYMBOL_TO_HIDE = PROGRESSION[random.randint(0, 9)]
    question = PROGRESSION.copy()
    question[question.index(SYMBOL_TO_HIDE)] = '..'
    print('Question: {}'.format(question))
    USER_ANSWER = prompt.integer('Your answer: ')
    if USER_ANSWER == SYMBOL_TO_HIDE:
        print('Correct!')
        return True
    else:
        result = '\"{}\" is wrong answer ;(. Correct answer was \"{}\"'
        print(result.format(USER_ANSWER, SYMBOL_TO_HIDE))
        return False
