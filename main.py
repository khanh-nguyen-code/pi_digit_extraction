from pi_digit_extraction import nth_digit_hex, hex2dec
import multiprocessing as mp
int2hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
pool = mp.Pool()
N = 10000
hex_list = pool.map(nth_digit_hex, range(N))

# take N digits
print("https://github.com/khanhhhh/pi_digit_extraction")
print("3.", end="", flush=True)
dec = hex2dec(hex_list)
for n in range(N):
    print(next(dec), end="", flush=True)
print()
