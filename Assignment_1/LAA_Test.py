import math

from numpy import *

data = [[-1, -2, 1, 2, 1, -2, 0, 2, 2, 1, 2],  # Guy
        [-1, -2, 2, 0, -2, -2, 1, 0, -1, 1, 2],  # Akvile
        [-2, -2, 2, 1, -2, -2, -2, 1, 1, 0, 1],  # Remi
        [-2, 0, 2, 1, -2, 1, -1, 0, 1, 0, 2],  # Joris
        [-1, -2, 1, 0, -1, -2, -2, 2, -2, -1, 1],  # Jannik
        [-2, -1, 1, 1, 2, 2]]  # Damyan

test = [-2, -1, 1, 1, 2, 2, 0, -2, -2, 0, 2]

magnitude_mystery = math.sqrt(sum([x ** 2 for x in data[-1]]))
magnitude_test = math.sqrt(sum([x ** 2 for x in test]))


def compute_likeliness():
    result = []
    for i in range(len(data) - 1):
        dot_product = sum(list(x * y for x, y in zip(data[i], data[-1])))
        magnitude_vector = math.sqrt(sum([x ** 2 for x in data[i][:len(data[-1])]]))
        result.append(dot_product / (magnitude_vector * magnitude_mystery))
    return result


def generate_likeliness():
    result = compute_likeliness()
    best_taste_index = result.index(max(result))
    return data[-1] + data[best_taste_index][len(data[-1]):]


def generate_score():
    dot_product = sum(list(x * y for x, y in zip(generate_likeliness(), test)))
    magnitude_vector = math.sqrt(sum([x ** 2 for x in generate_likeliness()]))

    return dot_product / (magnitude_vector * magnitude_test)


print(math.acos(generate_score()) * 180/math.pi)
