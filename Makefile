all: pi_bbp_build hex2dec_build

pi_bbp_build:
	rm -f pi_bbp
	go build pi_bbp.go

hex2dec_build:
	rm -f hex2dec
	g++ -g -std=c++17 hex2dec.cpp -o hex2dec
