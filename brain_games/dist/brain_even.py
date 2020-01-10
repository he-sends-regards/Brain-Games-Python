import prompt


def run():
    print('Answer "yes" if number even otherwise answer "no".\n')
    name = prompt.string('May I have your name? ')
    print('\nHello, {}!'.format(name))
    return
