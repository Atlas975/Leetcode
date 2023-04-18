#
# @lc app=leetcode id=1162 lang=python3
#
# [1162] As Far from Land as Possible
#

# @lc code=start
from collections import deque
from itertools import product


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque((i, j) for i, j in product(range(n), range(m)) if grid[i][j] == 1)
        if len(q) == n * m:
            return -1
        
        def expand(i, j, valididx):
            if valididx and grid[i][j] == 0:
                grid[i][j] = 1
                q.append((i, j))
                         
        dist = -1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                expand(i - 1, j, i > 0)
                expand(i + 1, j, i < n - 1)
                expand(i, j - 1, j > 0)
                expand(i, j + 1, j < m - 1)
            dist += 1
        return dist


# @lc code=end
