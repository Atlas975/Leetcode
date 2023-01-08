#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from collections import deque


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(op, cl):
            if op < n:
                s.append("(")
                dfs(op + 1, cl)
                s.pop()
            if cl < op:
                s.append(")")
                dfs(op, cl + 1)
                s.pop()
            if op == cl == n:
                res.append("".join(s))

        res, s = deque(), deque()
        dfs(0, 0)
        return res


# @lc code=end
