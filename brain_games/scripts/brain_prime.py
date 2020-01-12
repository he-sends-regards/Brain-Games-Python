import prompt
from brain_games.games.brain_prime import run


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no"\n')
    NAME = prompt.string('May I have your name? ')
    print('\nHello, {}!\n'.format(NAME))
    ROUNDS_NUM = 3
    run(ROUNDS_NUM, NAME)


if __name__ == '__main__':
    main()
