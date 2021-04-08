# PI DIGIT EXTRACTION

Calculate digits of pi using spigot algorithm on BPP formula

# PI REFERENCE

https://pi2e.ch/blog/2017/03/10/pi-digits-download/

# TEST

``` bash
python pi_bbp.py <number of digits> | python compare.py pi_hex_1m.txt
python pi_bbp.py <number of digits> | python hex2dec.py <number of digits> | python compare.py pi_dec_1m.txt
python pi_bbp_iter.py <number of digits> | python compare.py pi_hex_1m.txt
python pi_gibbons_iter.py <number of digits> | python compare.py pi_dec_1m.txt
```
