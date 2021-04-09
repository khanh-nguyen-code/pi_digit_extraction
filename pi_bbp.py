import sys

from digit_extraction.digit_extraction import pi_bbp

N = 1
if len(sys.argv) >= 2:
    N = int(sys.argv[1])

hex2char = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
for n in range(N):
    digit = pi_bbp(n)
    print(f"{hex2char[digit]}")
