from brain_games.engine import run
from brain_games.games.calc import generate_round


def main():
    run("What is the result of the expression?", generate_round)


if __name__ == "__main__":
    main()
