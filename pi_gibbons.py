import sys

from digit_extraction import pi_gibbons_iter

if __name__ == "__main__":
    base = 10
    N = 1
    if len(sys.argv) >= 2:
        N = int(sys.argv[1])
    pi = pi_gibbons_iter(base=base)
    for _ in range(N):
        print(f"{next(pi)}", end="")
    print()
