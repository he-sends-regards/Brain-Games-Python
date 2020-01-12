import prompt
from brain_games.games.brain_progression import run


def main():
    print('Welcome to the Brain Games!')
    print('Find missed element of the progression')
    NAME = prompt.string('May I have your name? ')
    print('\nHello, {}!\n'.format(NAME))
    ROUNDS_NUM = 3
    run(ROUNDS_NUM, NAME)


if __name__ == 'main':
    main()
