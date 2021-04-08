from digit_extraction import pi_gibbons_iter

if __name__ == "__main__":
    base = 10
    pi = pi_gibbons_iter(base=base)
    for digit in pi:
        print(f"{digit}")
