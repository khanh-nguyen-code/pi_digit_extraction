import multiprocessing as mp
import random
import sys

from digit_extraction import pi_bbp

if __name__ == "__main__":
    N = 1
    if len(sys.argv) >= 2:
        N = int(sys.argv[1])

    index_list = list(range(N))
    random.shuffle(index_list)

    pool = mp.Pool()
    hex_list = pool.map(pi_bbp, index_list)
    pool.close()
    hex_list = list(map(lambda pair: pair[1], sorted(zip(index_list, hex_list), key=lambda pair: pair[0])))

    hex2char = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    for digit in hex_list:
        print(f"{hex2char[digit]}")
