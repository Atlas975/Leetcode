#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
from functools import cache


class Solution:
    def fib(self, n: int) -> int:
        # a,b=0,1
        # for _ in range(n):
        #     a,b=b,a+b
        # return a

        @cache
        def fib(n):
            return n if n < 2 else fib(n - 1) + fib(n - 2)

        return fib(n)


# @lc code=end
