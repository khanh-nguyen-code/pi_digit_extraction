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
func sumX(n *big.Int, x *big.Int, eps uint) *big.Int {
	var shift = eps + uint(n.BitLen())
	var modulo = (&big.Int{}).Lsh(i1, shift)
	var k = big.NewInt(0)
	var numerator *big.Int
	var denominator *big.Int
	var numeratorInv *big.Int
	// finite sum
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
	var eps uint = 12
	var shift = eps + uint(n.BitLen())
	var modulo = (&big.Int{}).Lsh(i1, shift)
	var frac = (&big.Int{}).Mul(modulo, i8)
	var sum1 = sumX(n, i1, eps)
	var sum4 = sumX(n, i4, eps)
	var sum5 = sumX(n, i5, eps)
	var sum6 = sumX(n, i6, eps)
	frac.Add(frac, sum1.Mul(sum1, i4))
	frac.Sub(frac, sum4.Mul(sum4, i2))
	frac.Sub(frac, sum5)
	frac.Sub(frac, sum6) // frac = 4sum1 - 2sum4 - sum5 - sum6
	frac.Mod(frac, modulo)
	frac.Mul(i16, frac)
	frac.Rsh(frac, shift)
	var digit = int(frac.Int64())
	return digit
}
