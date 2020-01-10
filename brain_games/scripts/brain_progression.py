import prompt
from brain_games.games.brain_progression import run


def main():
    print('Welcome to the Brain Games!')
    print('Find missed element of the progression')
    name = prompt.string('May I have your name? ')
    print('\nHello, {}!\n'.format(name))
    rounds_num = 3
    run(rounds_num, name)


if __name__ == 'main':
    main()
