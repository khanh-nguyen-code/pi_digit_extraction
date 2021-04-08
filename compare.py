import sys


def read_pi(filename: str) -> str:
    with open(filename, "r") as f:
        pi = next(f).split("\n")[0]
    return pi


file_reference = "pi_reference.txt"

pi_reference = read_pi(file_reference)
i = 0
while True:
    try:
        digit = input()
    except EOFError:
        print("all ok")
        break
    if pi_reference[i] != digit:
        raise Exception(f"wrong digit at index {i}: expected '{pi_reference[i]}', actual '{digit}'")
    print(f"correct digit at index {i}: digit {digit}")
    i += 1
