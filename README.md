# PI DIGIT EXTRACTION

Calculate digits of pi using spigot algorithm on BPP formula to an arbitrary precision (all integers algorithm)

# PI REFERENCE

https://pi2e.ch/blog/2017/03/10/pi-digits-download/

# GET N-TH HEX DIGIT

calculate n-th hex digit

- python hex_digit.py <N>

# TEST

- <hex generator> <number of digits> | <comparator> pi_hex_1m.txt
- <hex generator> <number of digits> | <converter> | <comparator> pi_dec_1m.txt
- <dec generator> <number of digits> | <comparator> pi_dec_1m.txt

## <hex generator>

- python pi_bbp.py

- python pi_bbp_parallel.py

- python pi_bbp_iter.py

## <dec generator>

- python pi_gibbons_iter.py

## CONVERT HEX TO DEC

- hex2dec.cpp

## COMPARE WITH REFERENCES

- python compare.py