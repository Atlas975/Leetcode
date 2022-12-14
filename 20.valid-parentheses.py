#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        pairmp = {"(": ")", "[": "]", "{": "}"}
        stack = deque()

        for c in s:
            if c in pairmp:
                stack.append(c)
            elif not stack or pairmp[stack.pop()] != c:
                return False
        return not stack


# @lc code=end
