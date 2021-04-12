const readline = require("readline");

const i10 = BigInt(10);

const hex2char = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"];

function hex2dec(hex_list = []) {
    let dec_list = [];

    let h = BigInt("0x" + hex_list.map(function (num) {
        return hex2char[num];
    }).join(""));
    const l = BigInt(4 * hex_list.length);
    for (let i=0; i<hex_list.length; i++) {
        const digit = (h * i10) >> l;
        dec_list.push(Number(digit));
        h = (h * i10) - (digit << l);
    }
    return dec_list;
}

let N;
if (process.argv.length >= 3) {
    N = Number(process.argv[2]);
}

const rl = readline.createInterface({
    input: process.stdin,
    output: null,
});

let hex_list = [];

const char2hex = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15
};

rl.on("line", function (input) {
    hex_list.push(char2hex[input]);
    if (hex_list.length === N) {
        rl.close();
    }
});
rl.on("close", function () {
    const dec_list = hex2dec(hex_list);
    for (let i=0; i<dec_list.length; i++) {
        console.log(dec_list[i]);
    }
});
