from brain_games.engine import run
from brain_games.games.progression import generate_round


def main():
    run("What number is missing in the progression?", generate_round)


if __name__ == "__main__":
    main()
