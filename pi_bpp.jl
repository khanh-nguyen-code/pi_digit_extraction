include("digit_extraction/digit_extraction.jl")

n = 1

hex2char = Dict([
    0 => "0",
    1 => "1",
    2 => "2",
    3 => "3",
    4 => "4",
    5 => "5",
    6 => "6",
    7 => "7",
    8 => "8",
    9 => "9",
    10 => "a",
    11 => "b",
    12 => "c",
    13 => "d",
    14 => "e",
    15 => "f",
])

N = UInt64(1)
if length(ARGS) ≥ 1
    N = parse(UInt64, ARGS[1])
end
for n ∈ 0:N-1
    digit = DigitExtraction.pi_bbp(n)
    println("$(hex2char[digit])")
end