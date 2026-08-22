import math
import random


def generate_round():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    return f"{first} {second}", math.gcd(first, second)
