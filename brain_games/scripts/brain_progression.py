from brain_games.games import brain_progression
from brain_games import engine


def main():
    engine.run(brain_progression.DESCRIPTION, brain_progression)
    return


if __name__ == '__main__':
    main()
