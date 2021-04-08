import sys

def read_pi(filename: str) -> str:
    pi = ""
    with open(filename, "r") as f:
        pi = next(f).split("\n")[0]
    return pi

file_reference = "pi_reference.txt"

pi_reference = read_pi(file_reference)
pi_test = input().split("\n")[0]
for i, digit in enumerate(pi_test):
    if pi_reference[i] != digit:
        raise Exception(f"wrong digit at {i}, expected '{pi_reference[i]}', actual '{digit}'")
print("all ok")
