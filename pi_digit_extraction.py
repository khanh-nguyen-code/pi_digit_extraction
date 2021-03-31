# Created by Khanh Nguyen Ngoc on 31/3/21.

"""
pi digit extraction
Given BPP formula
\pi = 4 s_1 - 2 s_4 - s_5 - s_6
where s_x = \sum_{k=0}^{\infty} \frac{16^{-k}}{8k+x}
"""


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


def nth_digit_hex(n: int) -> int:
    frac = (4 * sum_x(n, 1) - 2 * sum_x(n, 4) - sum_x(n, 5) - sum_x(n, 6)) % 1
    digit = int(16 * frac)
    return digit


if __name__ == "__main__":
    int2hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    n = 0
    while n <= 1000:
        digit = nth_digit_hex(n)
        print(f"{n} -> {int2hex[digit]}")
        n += 1
