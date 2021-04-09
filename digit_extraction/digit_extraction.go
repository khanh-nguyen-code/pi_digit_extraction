package digit_extraction

import (
	"math/big"
)

// sumX : the fractional part of
//        16^n s_x = 16^n \sum_{k=0}^{\infty} \frac{1}{16^k (8k+x)}
// let b be the number of bits of n
// shift = eps + b
// result is represented as a fixed-point number.
// example: if shift is 2
// 			big.Int 12345 is equivalent to 123.45
func sumX(n *big.Int, x *big.Int, eps int) *big.Int {
	var k = big.NewInt(0)
	// finite sum
	var shift = uint(eps + n.BitLen())
	var modulo = (&big.Int{}).Lsh(i1, shift)
	var s1 = big.NewInt(0)
	for k.Cmp(n) != +1 {
		denominator := (&big.Int{}).Add((&big.Int{}).Mul(i8, k), x)             // 8k+x
		numerator := (&big.Int{}).Exp(i16, (&big.Int{}).Sub(n, k), denominator) // 16^{n-k} mod 8k+x
		numerator = numerator.Mod(numerator, denominator)
		numerator = numerator.Lsh(numerator, shift)
		numerator = numerator.Div(numerator, denominator)
		s1 = s1.Add(s1, numerator)
		s1 = s1.Mod(s1, modulo)
		k = k.Add(k, i1)
	}
	// infinite sum
	var s2 = big.NewInt(0)
	for {
		denominator := (&big.Int{}).Add((&big.Int{}).Mul(i8, k), x)        // 8k+x
		numeratorInv := (&big.Int{}).Exp(i16, (&big.Int{}).Sub(k, n), nil) // 16^{k-n}
		denominator = denominator.Mul(denominator, numeratorInv)
		if denominator.Cmp(modulo) == +1 {
			break
		}
		s2 = s2.Add(s2, (&big.Int{}).Div(modulo, denominator))
		k = k.Add(k, i1)
	}
	return (&big.Int{}).Mod((&big.Int{}).Add(s1, s2), modulo)
}

// PiBPP : return n-th digit of PI in hexadecimal
func PiBPP(n *big.Int) int {
	var eps = 12
	var frac = big.NewInt(0)
	var shift = uint(eps + n.BitLen())
	var modulo = (&big.Int{}).Lsh(i1, shift)
	frac = frac.Add(frac, (&big.Int{}).Mul(i4, sumX(n, i1, eps)))
	frac = frac.Sub(frac, (&big.Int{}).Mul(i2, sumX(n, i4, eps)))
	frac = frac.Sub(frac, sumX(n, i5, eps))
	frac = frac.Sub(frac, sumX(n, i6, eps))
	frac = frac.Mod(frac, modulo)
	frac = frac.Mul(i16, frac)
	frac = frac.Rsh(frac, shift)
	var digit = int(frac.Int64())
	return digit
}
