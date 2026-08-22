import random


def generate_round():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    hidden_index = random.randrange(length)
    progression = [start + step * index for index in range(length)]
    answer = progression[hidden_index]
    progression[hidden_index] = ".."
    return " ".join(map(str, progression)), answer
