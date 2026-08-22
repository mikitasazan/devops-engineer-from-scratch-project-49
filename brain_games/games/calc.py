import random

OPERATIONS = ("+", "-", "*")


def generate_round():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    operation = random.choice(OPERATIONS)
    expression = f"{first} {operation} {second}"

    if operation == "+":
        answer = first + second
    elif operation == "-":
        answer = first - second
    else:
        answer = first * second

    return expression, answer
