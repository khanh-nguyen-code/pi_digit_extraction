//
// Created by Khanh Nguyen Ngoc on 19/3/21.
//

#ifndef PI_DIGIT_EXTRACTION_PI_DIGIT_EXTRACTION_H
#define PI_DIGIT_EXTRACTION_PI_DIGIT_EXTRACTION_H

/* pi digit extraction
 * Given BPP formula
 * \pi = \Sigma_{k=0}^{\infty} \frac{1}{16^k} (\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6})
 * or
 * \pi = 4 s_1 - 2 s_4 - s_5 - s_6
 */

#include <cmath>

namespace extraction {
    /*
    int power_mod(int a, int n, int p) {
        // return a^n mod p
        int out = 1;
        for (int i = 0; i < n; i++) {
            out *= a;
            out = out % p;
        }
        return out;
    }
    */
    int power_mod(int a, int n, int p) {
        // return a^n mod p
        int out = 1;
        a = a % p;
        if (a == 0) {
            return 0;
        }
        while (n > 0) {
            if (n % 2 == 1) {
                out = (out * a) % p;
            }
            n /= 2;
            a = (a * a) % p;
        }
        return out;
    }


    float power_frac(int a, int n) {
        // return a^-n
        float out = 1.0;
        for (int i = 0; i < n; i++) {
            out /= float(a);
        }
        return out;
    }

    float fraction(float x) {
        return x - std::floor(x);
    }

    float sum_x(int n, int x, float eps = 0) {
        // return the fractional part of  16^n \Sigma_{k=0}^{\infty} \frac{1}{16^k (8k+x)} = 16^n s_x
        // finite sum
        float s1 = 0.0;
        for (int k = 0; k <= n; k++) {
            int numerator = power_mod(16, n - k, 8 * k + x);
            int denominator = 8 * k + x;
            float term = float(numerator) / float(denominator);
            s1 += term;
            s1 = fraction(s1);
        }
        // infinite sum
        float s2 = 0.0;
        for (int k = n + 1;; k++) {
            float numerator = power_frac(16, -(n - k));
            int denominator = 8 * k + x;
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
