import random


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def generate_round():
    number = random.randint(1, 100)
    return number, "yes" if is_prime(number) else "no"
