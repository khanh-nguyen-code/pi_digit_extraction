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


if __name__ == "__main__":
    int2hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    import time

    t1 = time.time()
    n = 0
    while n < 100:
        digit = nth_digit_hex(n)
        print(int2hex[digit], end="")
        n += 1
    t2 = time.time()
    print(f"\nelapsed time: {t2 - t1}")
    t1 = time.time()
    for n, digit in enumerate(pi_bbp()):
        if n >= 100:
            break
        print(int2hex[digit], end="")
    t2 = time.time()
    print(f"\nelapsed time: {t2 - t1}")
