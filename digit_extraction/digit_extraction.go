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
	var numerator *big.Int
	var denominator *big.Int
	var numeratorInv *big.Int
	// finite sum
	var shift = uint(eps + n.BitLen())
	var modulo = (&big.Int{}).Lsh(i1, shift)
	var sum = big.NewInt(0)
	for k.Cmp(n) != +1 {
		denominator = big.NewInt(8)
		denominator.Mul(denominator, k)
		denominator.Add(denominator, x) // 8k+x
		numerator = (&big.Int{}).Sub(n, k)
		numerator.Exp(i16, numerator, denominator) // 16^{n-k} mod 8k+x
		numerator.Mod(numerator, denominator)      // remove decimal part from numerator / denominator
		numerator.Lsh(numerator, shift)            // shift left: multiply by modulo
		numerator.Div(numerator, denominator)      // integer division
		sum.Add(sum, numerator)                    // add to the sum
		sum.Mod(sum, modulo)                       // remove decimal part
		k.Add(k, i1)
	}
	// infinite sum
	for {
		denominator = big.NewInt(8)
		denominator.Mul(denominator, k)
		denominator.Add(denominator, x) // 8k+x
		numeratorInv = (&big.Int{}).Sub(k, n)
		numeratorInv.Exp(i16, numeratorInv, nil) // 16^{k-n}
		denominator.Mul(denominator, numeratorInv)
		if denominator.Cmp(modulo) == +1 { // quotient is zero after that, break
			break
		}
		numerator = (&big.Int{}).Add(modulo, i0) // numerator after shift left = modulo
		numerator.Div(numerator, denominator)    // integer division
		sum.Add(sum, numerator)
		k.Add(k, i1)
	}
	return sum.Mod(sum, modulo)
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
