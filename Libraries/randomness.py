import random

cards = ["Jack", "Queen", "King"]


def main():
    # print(random.choice(cards))
    # print(random.choices(cards, weights=[75, 15, 10], k=2))
    # random.seed(1)
    # print(random.sample(cards, k=2))
    print(random.choices(range(1, 7), k=2))


def gen_hex_color():
    HEX_DIGIT = [
        "0", "1", "2",
        "3", "4", "5",
        "6", "7", "8",
        "9", "a", "b",
        "c", "d", "e",
        "f",
    ]

    curr_digit = random.sample(HEX_DIGIT, k=6)
    hex_code = "#"
    for digit in curr_digit:
        hex_code += digit

    return hex_code


main()
