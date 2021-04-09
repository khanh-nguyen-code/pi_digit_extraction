import sys


def read_pi(filename: str) -> str:
    with open(filename, "r") as f:
        pi = next(f).split("\n")[0]
    return pi


file_reference = "pi_dec_1m.txt"

if len(sys.argv) >= 2:
    file_reference = sys.argv[1]

pi_reference = read_pi(file_reference)
for char in pi_reference:
    print(f"{char}")
