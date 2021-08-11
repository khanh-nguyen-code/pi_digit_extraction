.PHONY: hex2dec_build

hex2dec_build:
	rm -f hex2dec
	g++ -O3 -std=c++17 hex2dec.cpp -o hex2dec
