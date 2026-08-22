import random

import prompt

from brain_games.cli import welcome_user


def is_even(number):
    return number % 2 == 0


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        number = random.randint(1, 100)
        correct_answer = "yes" if is_even(number) else "no"
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ").lower()

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
