package main

import (
	"flag"
	"fmt"
	"github.com/khanhhhh/pi_digit_extraction/digit_extraction"
	"math/big"
)

func main() {
	var hex2char = [16]string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"}
	flag.Parse()
	args := flag.Args()
	var n = big.NewInt(1)
	if len(args) >= 1 {
		temp, ok := (&big.Int{}).SetString(args[0], 10)
		if ok {
			n = temp
		}
	}
	fmt.Println(hex2char[digit_extraction.PiBPP(n)])
}
