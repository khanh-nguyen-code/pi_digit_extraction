import sys
import multiprocessing as mp
import random
from typing import List, Iterator, Tuple

from digit_extraction import pi_gibbons_iter


def hex2dec(hex_list: List[int]) -> Iterator[int]:
    """
    multiply the hex by 10, the result before the decimal point should be the same
    let x = 0.h1h2h3h4 be the hexadecimal representation
    0.h1h2h3h4 x 10 = h0'.h1'h2'h3'h4'
    let x = 0.d1d2d3d4 be the decimal representation
    0.d1d2d3d4 x 10 = d1.d1d2d3 0
    d1 = h0'
    keep multiply the hexadecimal representation by 10, we will get the correct decimal representation
    :param length:
    :param hex_list:
    :return:
    """

    def reduce(hex_list: List[int]) -> List[int]:
        while True:
            if len(hex_list) == 0:
                break
            if hex_list[len(hex_list) - 1] != 0:
                break
            hex_list = hex_list[:len(hex_list) - 1]
        return hex_list

    def canvas_add(list1: List[int], list2: List[int]):
        if len(list1) != len(list2):
            raise Exception("list1 and list2 must have the same length")

        def adder3(a: int, b: int, c: int) -> Tuple[int, int]:
            return divmod(a + b + c, 16)

        carry = 0
        for i in range(len(list1) - 1, -1, -1):
            carry, list1[i] = adder3(list1[i], list2[i], carry)
        return carry

    def mul10(hex_list: List[int]) -> int:
        carry = 0
        copied = [*hex_list]
        for _ in range(9):
            carry += canvas_add(hex_list, copied)
        return carry

    while True:
        hex_list = reduce(hex_list)
        if len(hex_list) == 0:
            break
        yield mul10(hex_list)


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
