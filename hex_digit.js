const {PiBBP} = require("./digit_extraction/digit_extraction");

let N = BigInt(1);
if (process.argv.length >= 3) {
    N = BigInt(process.argv[2]);
}

const hex2char = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
console.log(hex2char[PiBBP(n)]);
