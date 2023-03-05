#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = deque()
        for t in tokens:
            match (t):
                case "+":
                    s.append(s.pop() + s.pop())
                case "-":
                    s.append(-s.pop() + s.pop())
                case "*":
                    s.append(s.pop() * s.pop())
                case "/":
                    s.append((1 / s.pop()) * s.pop())
                case _:
                    s.append(int(t))
        return s.pop()
