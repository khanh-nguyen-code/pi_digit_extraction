if __name__ == "__main__":
    from pi_digit_extraction import pi_digit, hex2dec
    import multiprocessing as mp
    import random

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
