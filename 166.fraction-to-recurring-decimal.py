#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ""
        if (numerator < 0) ^ (denominator < 0):
            res += "-"
        if numerator % denominator == 0:
            return str(numerator // denominator)
        num = str(numerator / denominator).split(".")
        frac = num[1]
        rep = len(frac) // 2
        for i in range(rep):
            if frac[i] == frac[i + 1]:
                rep = i
                break

        if frac[:rep] == frac[rep:]:
            return f"{num[0]}.({frac[:rep]})"
        return f"{num[0]}.{frac}"


# @lc code=end
