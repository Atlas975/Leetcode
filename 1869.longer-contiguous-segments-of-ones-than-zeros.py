#
# @lc app=leetcode id=1869 lang=python3
#
# [1869] Longer Contiguous Segments of Ones than Zeros
#

# @lc code=start
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max1 = max0 = cur1 = cur0 = 0
        for c in s:
            if c == "1":
                cur1 += 1
                cur0 = 0
            else:
                cur0 += 1
                cur1 = 0
            max1, max0 = max(max1, cur1), max(max0, cur0)
        return max1 > max0


# @lc code=end
