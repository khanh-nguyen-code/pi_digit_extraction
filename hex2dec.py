import sys
import multiprocessing as mp
import random
from typing import List, Iterator, Tuple

from digit_extraction import pi_gibbons_iter




if __name__ == "__main__":

    char_list = input().split("\n")[0]
    char2hex = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15,
    }
    hex_list = [char2hex[char] for char in char_list]
    dec_iter = hex2dec(hex_list)
    for _ in range(len(hex_list)):
        print(f"{next(dec_iter)}", end="")
    print()
