#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        res = l = 0
        for r, c in enumerate(bin(n)[2:]):
            if c == "1":
                res = max(res, r - l)
                l = r
        return res


# @lc code=end
