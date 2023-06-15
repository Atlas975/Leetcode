#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#

# @lc code=start
from itertools import product


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if grid[i][j] == 1:
                return True
            grid[i][j] = 1
            l = dfs(i - 1, j) if i > 0 else False
            r = dfs(i + 1, j) if i < n - 1 else False
            u = dfs(i, j - 1) if j > 0 else False
            d = dfs(i, j + 1) if j < m - 1 else False
            return l and r and u and d

        return sum(dfs(i, j) for i, j in product(range(n), range(m)) if grid[i][j] == 0)


# @lc code=end
