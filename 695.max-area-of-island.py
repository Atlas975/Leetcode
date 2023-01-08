#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start

from itertools import product


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = 0
            return 1 + sum(
                dfs(dr, dc)
                for dr, dc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
                if 0 <= dr < n and 0 <= dc < m and grid[dr][dc]
            )

        return max(
            (dfs(r, c) for r, c in product(range(n), range(m)) if grid[r][c] == 1),
            default=0,
        )


# @lc code=end
