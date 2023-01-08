#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start


class Solution:
    def myAtoi(self, s: str) -> int:
        sign, i = 1, 0

        s = s.lstrip()
        n = len(s)
        if n == 0:
            return 0

        if s[i] in {"-", "+"}:
            sign = 1 - 2 * (s[i] == "-")
            i += 1

        base = 0
        while i < n and s[i].isdigit():
            base = base * 10 + int(s[i])
            i += 1

        base *= sign

        if base > 2**31 - 1:
            return 2**31 - 1
        elif base < -(2**31):
            return -(2**31)
        return base


# @lc code=end
