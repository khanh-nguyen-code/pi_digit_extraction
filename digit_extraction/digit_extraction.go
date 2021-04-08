package digit_extraction

import (
	"math"
	"math/big"
)

// frac : return the fractional part of a/b
func frac(a *big.Int, b *big.Int) float64 {
	a = a.Mod(a, b)
	bitLen := b.BitLen()
	if bitLen > 53 {
		b = b.Rsh(b, uint(bitLen-53))
		a = a.Rsh(a, uint(bitLen-53))
	}
	return float64(a.Int64()) / float64(b.Int64())
}

// sumX : the fractional part of
//        16^n s_x = 16^n \sum_{k=0}^{\infty} \frac{1}{16^k (8k+x)}
var sixteen = big.NewInt(16)
var eight = big.NewInt(8)
var one = big.NewInt(1)
var four = big.NewInt(4)
var five = big.NewInt(5)
var six = big.NewInt(6)

func sumX(n *big.Int, x *big.Int) float64 {
	// finite sum
	var k = big.NewInt(0)
	var s1 float64 = 0
	for k.Cmp(n) != +1 {
		denominator := (&big.Int{}).Add((&big.Int{}).Mul(eight, k), x)
		numerator := (&big.Int{}).Exp(sixteen, (&big.Int{}).Sub(n, k), denominator)
		s1 += frac(numerator, denominator)
		if s1 >= 1 {
			s1 -= 1
		}
		k = k.Add(k, one)
	}
	// infinite sum
	var s2 float64 = 0
	for {
		denominator := (&big.Int{}).Add((&big.Int{}).Mul(eight, k), x)
		numeratorInv := (&big.Int{}).Exp(sixteen, (&big.Int{}).Sub(k, n), nil)
		denominator = denominator.Mul(denominator, numeratorInv)
		if denominator.BitLen() > 53 {
			break
		}
		s2 += 1 / float64(denominator.Int64())
		k = k.Add(k, one)
	}
	var s = s1 + s2
	if s >= 1 {
		s -= 1
	}
	return s
}
func PiBPP(n *big.Int) int {
	var frac = 4*sumX(n, one) - 2*sumX(n, four) - sumX(n, five) - sumX(n, six)
	frac -= math.Floor(frac)
	var digit = int(16 * frac)
	return digit
}
