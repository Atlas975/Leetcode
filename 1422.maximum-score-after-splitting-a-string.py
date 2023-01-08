#
# @lc app=leetcode id=1422 lang=python3
#
# [1422] Maximum Score After Splitting a String
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        zero = one = 0
        res = -1
        for num in s[:-1]:
            if num == "0":
                zero += 1
                res = max(res, zero + one)
            else:
                one -= 1
        if s[-1] == "1":
            one -= 1
        return res - one


# @lc code=end
