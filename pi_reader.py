import sys
from typing import Iterator


def read_pi(filename: str) -> Iterator[str]:
    with open(filename, "r") as f:
        while True:
            digit = f.read(1)
            if digit == "\n":
                break
            yield digit


file_reference = "pi_dec_1m.txt"
N = 1000000

if len(sys.argv) >= 2:
    file_reference = sys.argv[1]

if len(sys.argv) >= 3:
    N = int(sys.argv[2])

pi_reference = read_pi(file_reference)
for i, digit in enumerate(pi_reference):
    if i >= N:
        break
    print(f"{digit}")
