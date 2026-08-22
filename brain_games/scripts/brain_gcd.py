from brain_games.engine import run
from brain_games.games.gcd import generate_round


def main():
    run("Find the greatest common divisor of given numbers.", generate_round)


if __name__ == "__main__":
    main()
