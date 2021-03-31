# Created by Khanh Nguyen Ngoc on 31/3/21.

"""
pi digit extraction
Given BPP formula
\pi = 4 s_1 - 2 s_4 - s_5 - s_6
where s_x = \sum_{k=0}^{\infty} \frac{16^{-k}}{8k+x}
"""
from typing import List, Iterator, Tuple


def nth_digit_hex(n: int) -> int:
    def sum_x(n: int, x: int, eps: float = 1e-6) -> float:
        """
        :param n:
        :param x:
        :param eps:
        :return: the fractional part of
        16^n s_x = 16^n \sum_{k=0}^{\infty} \frac{1}{16^k (8k+x)}
        """
        k = 0
        # finite sum
        s1 = 0.0
        while k <= n:
            numerator = pow(16, n - k, 8 * k + x)
            denominator = 8 * k + x
            term = numerator / denominator
            s1 = (s1 + term) % 1
            k += 1
        # infinite sum
        s2 = 0.0
        while True:
            numerator = 16 ** (n - k)
            denominator = 8 * k + x
            term = numerator / denominator
            if term <= eps:
                break
            s2 += term
            k += 1
        return (s1 + s2) % 1

    frac = (4 * sum_x(n, 1) - 2 * sum_x(n, 4) - sum_x(n, 5) - sum_x(n, 6)) % 1
    digit = int(16 * frac)
    return digit


def pi_bbp():
    """
    Conjectured BBP generator of hex digits of pi
    https://possiblywrong.wordpress.com/2017/09/30/digits-of-pi-and-python-generators/
    :return:
    """
    a, b = 2, 15
    k = 1
    while True:
        ak, bk = (120 * k ** 2 + 151 * k + 47,
                  512 * k ** 4 + 1024 * k ** 3 + 712 * k ** 2 + 194 * k + 15)
        a, b = (16 * a * bk + ak * b, b * bk)
        digit, a = divmod(a, b)
        yield digit
        k = k + 1


def pi_gibbons(base=10):
    """
    Gibbons spigot generator of digits of pi in given base.
    https://possiblywrong.wordpress.com/2017/09/30/digits-of-pi-and-python-generators/
    :param base:
    :return:
    """
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < n * t:
            yield n
            q, r, t, k, n, l = (base * q, base * (r - n * t), t, k,
                                (base * (3 * q + r)) // t - base * n, l)
        else:
            q, r, t, k, n, l = (q * k, (2 * q + r) * l, t * l, k + 1,
                                (q * (7 * k + 2) + r * l) // (t * l), l + 2)


def hex2dec(hex_list: List[int], length: int) -> Iterator[int]:
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

    def adder3(a: int, b: int, c: int) -> Tuple[int, int]:
        return divmod(a + b + c, 16)

    def canvas_add(list1: List[int], list2: List[int]):
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

    for _ in range(length):
        yield mul10(hex_list)


if __name__ == "__main__":
    int2hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    hex_list = []
    for n in range(10):
        hex_list.append(nth_digit_hex(n))
    for digit in hex2dec(hex_list, 10):
        print(digit, end="", flush=True)
