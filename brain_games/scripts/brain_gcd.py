import prompt
from brain_games.games.brain_gcd import run


def main():
    print('Welcome to the Brain Games!')
    print('Find gcd of two numbers\n')
    NAME = prompt.string('May I have your name? ')
    print('\nHello, {}!\n'.format(NAME))
    ROUNDS_NUM = 3
    run(ROUNDS_NUM, NAME)


if __name__ == 'main':
    main()
