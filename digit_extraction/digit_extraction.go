package digit_extraction

import (
	"math"
	"math/big"
)

// we treat float64 as fixed point of 53 bits
var floatUnit = 53

// ratFrac : return the fractional part of a/b for a > 0 and b > 0
func ratFrac(a *big.Int, b *big.Int) float64 {
	// make a < b
	a = a.Mod(a, b)
	// if bit length of a and b larger than 53, shift right until they have at most 53 in order to convert into float64
	bitLen := b.BitLen()
	if bitLen > floatUnit {
		b = b.Rsh(b, uint(bitLen-floatUnit))
		a = a.Rsh(a, uint(bitLen-floatUnit))
	}
	return float64(a.Int64()) / float64(b.Int64())
}

// floatFrac : return the fractional part of x
// 1.3 -> 0.3, -1.3 -> 0.7
func floatFrac(x float64) float64 {
	_, f := math.Modf(x)
	if f < 0 {
		f += 1
	}
	return f
}

// sumX : the fractional part of
//        16^n s_x = 16^n \sum_{k=0}^{\infty} \frac{1}{16^k (8k+x)}
func sumX(n *big.Int, x *big.Int) float64 {
	// finite sum
	var k = big.NewInt(0)
	var s1 float64 = 0
	for k.Cmp(n) != +1 {
		denominator := (&big.Int{}).Add((&big.Int{}).Mul(i8, k), x)             // 8k+x
		numerator := (&big.Int{}).Exp(i16, (&big.Int{}).Sub(n, k), denominator) // 16^{n-k} mod 8k+x
		s1 += ratFrac(numerator, denominator)
		s1 = floatFrac(s1)
		k = k.Add(k, i1)
	}
	// infinite sum
	var s2 float64 = 0
	for {
		denominator := (&big.Int{}).Add((&big.Int{}).Mul(i8, k), x)        // 8k+x
		numeratorInv := (&big.Int{}).Exp(i16, (&big.Int{}).Sub(k, n), nil) // 16^{k-n}
		denominator = denominator.Mul(denominator, numeratorInv)
		if denominator.BitLen() > floatUnit {
			break
		}
		s2 += 1 / float64(denominator.Int64())
		k = k.Add(k, i1)
	}
	return floatFrac(s1 + s2)
}

// PiBPP : return n-th digit of PI in hexadecimal
func PiBPP(n *big.Int) int {
	var frac = floatFrac(4*sumX(n, i1) - 2*sumX(n, i4) - sumX(n, i5) - sumX(n, i6))
	var digit = int(16 * frac)
	return digit
}
