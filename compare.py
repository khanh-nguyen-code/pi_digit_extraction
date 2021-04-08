import sys

def read_pi(filename: str) -> str:
    pi = ""
    with open(filename, "r") as f:
        next(f)
        pi = next(f)
    return pi

file_reference = "pi_reference.txt"
file_test = "pi.txt"
if len(sys.argv) >= 2:
    file_test = sys.argv[1]

pi_reference = read_pi(file_reference)
pi_test = read_pi(file_test)
for i, digit in enumerate(pi_test):
    if pi_reference[i] != digit:
        raise Exception(f"wrong digit at {i}, expected {pi_reference[i]}, actual {digit}")

