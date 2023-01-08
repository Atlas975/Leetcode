#
# @lc app=leetcode id=397 lang=python3
#
# [397] Integer Replacement
#

# @lc code=start
class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            if n % 2 == 1:
                if ((n - 1) / 2) % 2 == 0:
                    n -= 1
                else:
                    n += 1
                continue
            if n % 2 == 0:
                n /= 2
                count += 1
                continue
        return count


# @lc code=end
