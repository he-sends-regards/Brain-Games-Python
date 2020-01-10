from brain_games.games.brain_calc import run
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?\n')
    name = prompt.string('May I have your name? ')
    print('\nHello, {}!\n'.format(name))
    rounds_num = 3
    run(rounds_num, name)


if __name__ == 'main':
    main()
