#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from itertools import product, starmap


class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(r, c, outbound=False):
            if outbound or grid[r][c] == "0":
                return 0
            grid[r][c] = "0"
            dfs(r - 1, c, r == 0)
            dfs(r + 1, c, r == n - 1)
            dfs(r, c - 1, c == 0)
            dfs(r, c + 1, c == m - 1)
            return 1
        return sum(starmap(dfs, product(range(n), range(m))))


# @lc code=end
