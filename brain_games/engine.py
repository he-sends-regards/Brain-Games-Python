import prompt


ROUNDS_NUM = 3


def greeting(description):
    print('Welcome to the Brain Games!')
    print(description)
    NAME = prompt.string('May I have your name? ')
    print('\nHello, {}!\n'.format(NAME))
    return NAME


def run(game_description, game):
    name = greeting(game_description)

    for i in range(ROUNDS_NUM):
        if game.run():
            continue
        else:
            print('Let\'s try again, {}'.format(name))
            return
    print('Congratulations, {}'.format(name))
