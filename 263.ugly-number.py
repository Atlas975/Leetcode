#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#


# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False

        sieve = (2, 3, 5)

        while n != 1:
            for f in sieve:
                if n % f == 0:
                    n = n // f
                    break
            else:
                return False

        return True


# @lc code=end
