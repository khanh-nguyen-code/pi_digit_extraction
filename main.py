if __name__ == "__main__":
    from pi_digit_extraction import pi_digit, hex2dec
    import multiprocessing as mp
    import numpy as np
    int2hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    pool = mp.Pool()
    N = 10000
    index_list = list(range(N))
    np.random.shuffle(index_list)
    argsort = np.argsort(index_list)
    hex_list = pool.map(pi_digit, index_list)
    hex_list = list(np.array(hex_list)[argsort])
    # take N digits
    print("https://github.com/khanhhhh/pi_digit_extraction")
    print("3.", end="", flush=True)
    dec = hex2dec(hex_list)
    for n in range(N):
        print(next(dec), end="", flush=True)
    print()
