import sys

from digit_extraction import pi_gibbons_iter

if __name__ == "__main__":
    base = 10
    for digit in pi_gibbons_iter(base=base):
        print(f"{digit}")
