#include "pi_digit_extraction.h"
#include <cstdio>
#include <array>
#include <string>

const std::array<std::string, 16> int2hex = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"};


int main() {
    int n = 0;
    while (n <= 10000) {
        int digit = extraction::nth_digit_hex(n);
        std::printf("%d: %s %d\n", n, int2hex[digit].c_str(), digit);
        //std::fflush(stdout);
        if (digit < 0 or digit >= 16) {
            break;
        }
        n++;
    }
    return 0;
}
