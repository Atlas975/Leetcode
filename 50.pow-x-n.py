#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def indice(x, n):
            if n == 0:
                return 1
            elif n % 2:
                return x * indice(x * x, n // 2)
            return indice(x * x, n // 2)

        res = indice(x, abs(n))
        return res if n > 0 else 1 / res


# @lc code=end
