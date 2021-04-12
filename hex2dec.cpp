#include<vector>
#include<tuple>
#include<iostream>
#include<map>

using digit = unsigned char;

std::tuple<digit, digit> adder3(digit a, digit b, digit c) {
    digit q = (a + b + c) / 16;
    digit r = (a + b + c) % 16;
    return {q, r};
}

digit canvas_add(std::vector<digit> &canvas, const std::vector<digit> &adder) {
    // canvas <- canvas + adder, return carry
    digit carry = 0;
    for (size_t i = canvas.size() - 1; i < canvas.size(); i--) {
        auto[q, r] = adder3(canvas[i], adder[i], carry);
        carry = q;
        canvas[i] = r;
    }
    return carry;
}

digit mul10(std::vector<digit> &canvas) {
    std::vector<digit> copied = canvas;
    digit total = 0;
    for (int i = 0; i < 9; i++) {
        total += canvas_add(canvas, copied);
    }
    return total;
}

std::vector<digit> hex2dec(std::vector<digit> &hex_list) {
    std::vector<digit> dec_list;
    dec_list.reserve(hex_list.size());
    for (size_t i = 0; i < hex_list.size(); i++) {
        dec_list.push_back(mul10(hex_list));
    }
    return dec_list;
}

std::map<char, digit> char2hex{
        {'0', 0},
        {'1', 1},
        {'2', 2},
        {'3', 3},
        {'4', 4},
        {'5', 5},
        {'6', 6},
        {'7', 7},
        {'8', 8},
        {'9', 9},
        {'a', 10},
        {'b', 11},
        {'c', 12},
        {'d', 13},
        {'e', 14},
        {'f', 15},
};

int main() {
    std::vector<digit> hex_list;
    for (std::string line; std::getline(std::cin, line);) {
        hex_list.push_back(char2hex[line[0]]);
    }

    auto dec_list = hex2dec(hex_list);
    for (size_t i = 0; i < dec_list.size(); i++) {
        std::cout << int(dec_list[i]) << std::endl;
    }
    return 0;
}