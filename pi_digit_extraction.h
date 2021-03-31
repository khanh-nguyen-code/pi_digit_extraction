//
// Created by Khanh Nguyen Ngoc on 19/3/21.
//

#ifndef PI_DIGIT_EXTRACTION_PI_DIGIT_EXTRACTION_H
#define PI_DIGIT_EXTRACTION_PI_DIGIT_EXTRACTION_H

/* pi digit extraction
 * Given BPP formula
 * \pi = \sum_{k=0}^{\infty} \frac{1}{16^k} (\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6})
 * or
 * \pi = 4 s_1 - 2 s_4 - s_5 - s_6
 */

#include <cmath>

namespace extraction {
    using uint = unsigned int;

    uint multiply_mod(uint a, uint b, uint p) {
        // return a*b mod p
        uint out = 0;
        a = a % p;
        b = b % p;
        while (b != 0) {
            if (b % 2 == 1) {
                out = (out + a) % p;
            }
            a = (a * 2) % p;
            b /= 2;
        }
        return out;
    }

    uint power_mod(uint a, uint n, uint p) {
        // return a^n mod p
        if (n == 0) {
            return 1;
        }
        uint out = 1;
        a = a % p;
        if (a == 0) {
            return 0;
        }
        while (n > 0) {
            if (n % 2 == 1) {
                // out = (out * a) % p;
                out = multiply_mod(out, a, p);
            }
            n /= 2;
            // a = (a * a) % p;
            a = multiply_mod(a, a, p);
        }
        return out;
    }


    float power_frac(uint a, uint n) {
        // return a^-n
        float out = 1.0;
        for (uint i = 0; i < n; i++) {
            out /= float(a);
        }
        return out;
    }

    float fraction(float x) {
        return x - std::floor(x);
    }

    float sum_x(uint n, uint x, float eps = 1e-6) {
        // return the fractional part of
        // 16^n \Sigma_{k=0}^{\infty} \frac{1}{16^k (8k+x)} = 16^n s_x

        // finite sum
        float s1 = 0.0;
        float s2 = 0.0;
        for (uint k = 0; k <= n; k++) {
            // finite sum
            uint numerator = power_mod(16, n - k, 8 * k + x);
            uint denominator = 8 * k + x;
            float term = float(numerator) / float(denominator);
            s1 += term;
            s1 = fraction(s1);
        }
        for (uint k = n + 1;; k++) {
            // infinite sum
            float numerator = power_frac(16, -(n - k));
            uint denominator = 8 * k + x;
            float term = float(numerator) / float(denominator);
            if (term <= eps) {
                break;
            }
            s2 += term;
        }

        return fraction(s1 + s2);
    }

    int nth_digit_hex(int n) {
        float frac = fraction(4 * sum_x(n, 1) - 2 * sum_x(n, 4) - sum_x(n, 5) - sum_x(n, 6));
        int digit = int(16 * frac);
        return digit;
    }

}
#endif //PI_DIGIT_EXTRACTION_PI_DIGIT_EXTRACTION_H
