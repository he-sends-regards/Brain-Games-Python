import random


DESCRIPTION = 'Find missed element of the progression'
PROGRESSION_LIMIT = 9


def make_progression():
    first_num_of_progression, d = random.randint(0, 10), random.randint(1, 10)
    result = [first_num_of_progression]
    for i in range(PROGRESSION_LIMIT):
        result.append(result[i] + d)
    return result


def make_question():
    progression_instance = make_progression()
    index = random.randint(0, 9)
    symb_to_hide = progression_instance[index]
    question = progression_instance.copy()
    question[question.index(symb_to_hide)] = '..'

    return str(question), str(progression_instance[index])
