from brain_games.games.brain_calc import run
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?\n')
    NAME = prompt.string('May I have your name? ')
    print('\nHello, {}!\n'.format(NAME))
    ROUNDS_NUM = 3
    run(ROUNDS_NUM, NAME)


if __name__ == 'main':
    main()
