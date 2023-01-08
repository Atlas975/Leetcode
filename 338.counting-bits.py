#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = [0] * (n + 1)
        res[0] = 0
        res[1] = 1
        for i in range(2, n + 1):
            res[i] = res[i // 2] if i % 2 == 0 else res[i // 2] + 1
        return res


# @lc code=end
