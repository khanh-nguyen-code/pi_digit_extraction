package main

import (
	"flag"
	"fmt"
	"github.com/khanhhhh/pi_digit_extraction/digit_extraction"
	"math/big"
)

var one = big.NewInt(1)

var hex2char = [16]string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"}

func main() {
	flag.Parse()
	args := flag.Args()
	var N = big.NewInt(1)
	if len(args) >= 1 {
		temp, ok := (&big.Int{}).SetString(args[0], 10)
		if ok {
			N = temp
		}
	}
	var n = big.NewInt(0)
	for n.Cmp(N) == -1 {
		fmt.Println(hex2char[digit_extraction.PiBPP(n)])
		n = n.Add(n, one)
	}
}
