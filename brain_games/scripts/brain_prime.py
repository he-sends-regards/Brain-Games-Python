from brain_games import engine
from brain_games.games import brain_prime


def main():
    engine.run(brain_prime.DESCRIPTION, brain_prime)
    return


if __name__ == '__main__':
    main()
