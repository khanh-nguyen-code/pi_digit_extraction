module DigitExtraction
    function pi_bbp(n::UInt64)::UInt8
        function sum_x(n::UInt64, x::UInt64)::Float64
            k::UInt64 = 0
            # finite sum
            s1::Float64 = 0.0
            while k ≤ n
                denominator = 8 * k + x
                numerator = powermod(16, n - k, denominator)
                term = numerator / denominator
                s1 = modf(s1 + term)[1]
                k += 1
            end
            # infinite sum
            s2::Float64 = 0.0
            while true
                denominator = 8 * k + x
                numerator = 16 ^ (n - k)
                term = numerator / denominator
                if term ≤ 0.0
                    break
                end
                s2 += term
                k += 1
            end
            return modf(s1 + s2)[1]
        end
        frac = modf(4 + 4 * sum_x(n, UInt64(1)) - 2 * sum_x(n, UInt64(4)) - sum_x(n, UInt64(5)) - sum_x(n, UInt64(6)))[1]
        digit = UInt8(modf(16 * frac)[2])
        return digit
    end
end