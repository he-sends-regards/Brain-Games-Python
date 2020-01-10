import prompt
import random


def run(rounds_num, name):
    for i in range(rounds_num):
        question = random.randint(1, 100)
        print('Question: {}'.format(question))

        def is_prime(num):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        return 'no'
                return 'yes'
            return 'no'

        correct_answer = is_prime(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            continue
        else:
            result = '\"{}\" is wrong answer ;(. Correct answer was \"{}\"'
            print(result.format(user_answer, correct_answer))
            return
    print('Congratulations, {}'.format(name))
    return
