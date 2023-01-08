#
# @lc app=leetcode id=1837 lang=python3
#
# [1837] Sum of Digits in Base K
#

# @lc code=start
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n > 0:
            res += n % k
            n //= k
        return res


# @lc code=end
