#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
from collections import deque


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k > n:
            return "0"
        s = deque()
        for c in num:
            while s and k > 0 and s[-1] > c:
                s.pop()
                k -= 1
            s.append(c)

        for _ in range(k):
            s.pop()
        return "".join(s).lstrip("0") or "0"


os


# @lc code=end
