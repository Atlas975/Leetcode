#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 5:
            return True
        for i in range(4, n // 2 + 1):
            if n % i == 0:
                if i in {2, 3, 5}:
                    return True
                else:
                    return False
        return False


# @lc code=end
