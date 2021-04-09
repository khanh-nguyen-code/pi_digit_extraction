all: hex_digit_build pi_bbp_build pi_bbp_parallel_build hex2dec_build

hex_digit_build:
	rm -f hex_digit
	go build hex_digit.go

pi_bbp_parallel_build:
	rm -f pi_bbp_parallel
	go build pi_bbp_parallel.go

pi_bbp_build:
	rm -f pi_bbp
	go build pi_bbp.go

hex2dec_build:
	rm -f hex2dec
	g++ -O3 -std=c++17 hex2dec.cpp -o hex2dec
