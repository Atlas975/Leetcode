#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start

from itertools import product, starmap


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(r, c):
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return (
                1
                + (dfs(r + 1, c) if r < n - 1 else 0)
                + (dfs(r - 1, c) if r > 0 else 0)
                + (dfs(r, c + 1) if c < m - 1 else 0)
                + (dfs(r, c - 1) if c > 0 else 0)
            )

        return max(starmap(dfs, product(range(n), range(m))))


# @lc code=end
