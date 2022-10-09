import numpy as np
from textwrap import wrap as split_every


def input_matrix():
    print("Coding matrix\n" + "_" * 20)
    user_input = input("")
    matrix = []
    while not user_input == "!":
        matrix.append(user_input)
        user_input = input("")
    out = '; '.join(matrix)
    return np.matrix(out)


def message_to_matrixes(message: str, split=3):
    message = split_every(message, split)
    new = []
    for original in message:
        replace_with = []
        for char in original:
            replace_with.append(TRANSLATION.index(char))
        while len(replace_with) != 3:
            replace_with.append(0)  # Solve dimension errors
        new.append(replace_with)
    return [np.matrix(m) for m in new]


SECRET = input_matrix()
MESSAGE = input("Message\n" + "_" * 20 + '\n').upper()
TRANSLATION = " ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$%^&*()-+=[]\\{}|;':\",./<>?`~"  # Indexes are the values used
TRANSLATED_MESSAGE = message_to_matrixes(MESSAGE)
# print(repr([m for m in TRANSLATED_MESSAGE]))
RESULT = [m * SECRET for m in TRANSLATED_MESSAGE]
print(*(r[0] for r in np.array(RESULT)), sep='\n')
