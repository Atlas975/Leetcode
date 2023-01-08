#
# @lc app=leetcode id=2328 lang=python3
#
# [2328] Number of Increasing Paths in a Grid
#

# @lc code=start
from functools import cache
from itertools import product, starmap


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        @cache
        def dfs(r, c):
            cur = grid[r][c]
            return 1 + sum(
                (
                    dfs(r + 1, c) if r + 1 < n and grid[r + 1][c] > cur else 0,
                    dfs(r - 1, c) if r >= 1 and grid[r - 1][c] > cur else 0,
                    dfs(r, c + 1) if c + 1 < m and grid[r][c + 1] > cur else 0,
                    dfs(r, c - 1) if c >= 1 and grid[r][c - 1] > cur else 0,
                )
            )

        return sum(starmap(dfs, product(range(n), range(m)))) % (10**9 + 7)


# @lc code=end
