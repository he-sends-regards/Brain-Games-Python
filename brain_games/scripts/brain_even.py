import prompt
from brain_games.games.brain_even import run


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".\n')
    name = prompt.string('May I have your name? ')
    print('\nHello, {}!\n'.format(name))
    rounds_num = 3
    run(rounds_num, name)


if __name__ == '__main__':
    main()
