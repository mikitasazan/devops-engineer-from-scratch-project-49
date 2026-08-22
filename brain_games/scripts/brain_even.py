import random

from brain_games.engine import run


def is_even(number):
    return number % 2 == 0


def main():
    def generate_round():
        number = random.randint(1, 100)
        return number, "yes" if is_even(number) else "no"

    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    run(description, generate_round)


if __name__ == "__main__":
    main()
