import sys
from typing import Tuple

from digit_extraction import pi_bbp
from pipeline import pipeline

if __name__ == "__main__":
    N = 1
    if len(sys.argv) >= 2:
        N = int(sys.argv[1])


    def mapping(n: int) -> Tuple[int, int]:
        return n, pi_bbp(n)


    data_in = iter(range(N))
    data_out = pipeline(
        data_in=data_in,
        mapping_list=[mapping],
        queue_size_list=[64, 64],
    )
    buffer = {}
    next_n = 0
    hex2char = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    for _ in range(N):
        digit = None
        if next_n in buffer:
            digit = buffer[next_n]
            buffer.pop(next_n)
        else:
            while True:
                n, d = next(data_out)
                if next_n == n:
                    digit = d
                    break
                else:
                    buffer[n] = d
        print(f"{hex2char[digit]}")
