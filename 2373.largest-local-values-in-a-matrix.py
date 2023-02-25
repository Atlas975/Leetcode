#
# @lc app=leetcode id=2373 lang=python3
#
# [2373] Largest Local Values in a Matrix
#

# @lc code=start
from itertools import product


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return [
            [max(grid[i][j] for i, j in product(range(x, x + 3), range(y, y + 3))) for y in range(len(grid[0]) - 2)]
            for x in range(len(grid) - 2)
        ]
