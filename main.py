import multiprocessing as mp
import random
from typing import List, Iterator, Tuple

from pi_digit_extraction import pi_digit


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
    int2hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    pool = mp.Pool()
    N = 1000
    index_list = list(range(N))
    random.shuffle(index_list)
    hex_list = pool.map(pi_digit, index_list)
    hex_list = [v for i, v in sorted(zip(index_list, hex_list))]
    # take N digits
    print("https://github.com/khanhhhh/pi_digit_extraction")
    print("3.", end="", flush=True)
    dec = hex2dec(hex_list)
    for n in range(N):
        print(next(dec), end="", flush=True)
    print()
