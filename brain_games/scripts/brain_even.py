from brain_games.games import brain_even
from brain_games import engine


def main():
    engine.run(brain_even.DESCRIPTION, brain_even)
    return


if __name__ == '__main__':
    main()
