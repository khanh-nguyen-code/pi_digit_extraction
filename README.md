# PI DIGIT EXTRACTION

Calculate digits of pi using spigot algorithm on BPP formula

# PI REFERENCE

https://pi2e.ch/blog/2017/03/10/pi-digits-download/

# TEST

- generator is hexadecimal

```
<generator> <number of digits> | <comparator> pi_hex_1m.txt
<generator> <number of digits> | <converter> <number of digits> | <comparator> pi_dec_1m.txt
```

- generator is decimal

```
<generator> <number of digits> | <comparator> pi_dec_1m.txt
```

## GENERATE HEX DIGITS

- `<generator>`

```
pi_bbp.py
pi_bbp_parallel.py
pi_bbp_iter.py
pi_bbp.go
pi_bbp_parallel.go
```  

## GENERATE DEC DIGITS

- `<generator>`

```
pi_gibbons_iter.py
```

## CONVERT HEX TO DEC

- `<converter>`

```
hex2dec.py
hex2dec.cpp
```

## COMPARE WITH REFERENCES

- `<comparator>`

```
compare.py
```

# EXAMPLE

```bash
make
./pi_bbp_parallel 1000 | ./hex2dec 1000 | python compare.py pi_dec_1m.txt
```