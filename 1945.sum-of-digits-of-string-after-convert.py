#
# @lc app=leetcode id=1945 lang=python3
#
# [1945] Sum of Digits of String After Convert
#

# @lc code=start
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        dig_sum = lambda x: sum(map(int, str(x)))
        res = dig_sum("".join((str(ord(c) - 96) for c in s)))
        for _ in range(k - 1):
            res = dig_sum(res)
        return res


# @lc code=end
