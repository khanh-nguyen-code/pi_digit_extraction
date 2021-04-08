import sys
import multiprocessing as mp
import random
from typing import List, Iterator, Tuple

from digit_extraction import pi_gibbons_iter, pi_bbp

if __name__ == "__main__":
    N = 1
    if len(sys.argv) >= 2:
        N = int(sys.argv[1])

    index_list = list(range(N))
    random.shuffle(index_list)
    pool = mp.Pool()
    hex_list = pool.map(pi_bbp, index_list)
    pool.close()
    hex_list = [v for i, v in sorted(zip(index_list, hex_list))]
    hex2char = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    for h in hex_list:
        print(f"{hex2char[h]}")
