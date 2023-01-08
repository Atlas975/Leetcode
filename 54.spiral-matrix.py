#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from collections import deque


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t, b = 0, len(matrix)
        l, r = 0, len(matrix[0])
        res = deque()
        while l < r and t < b:
            res.extend(matrix[t][i] for i in range(l, r))
            t += 1
            res.extend(matrix[i][r - 1] for i in range(t, b))
            r -= 1
            if l == r or t == b:
                break
            res.extend(matrix[b - 1][i] for i in reversed(range(l, r)))
            b -= 1
            res.extend(matrix[i][l] for i in reversed(range(t, b)))
            l += 1
        return res


# @lc code=end
