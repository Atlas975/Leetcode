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

        def dfs(r, c):
            if grid[r][c] != "1":
                return 0

            grid[r][c] = "0"
            for dr, dc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= dr < n and 0 <= dc < m: 
                    dfs(dr, dc)
            return 1

        return sum(starmap(dfs, product(range(n), range(m))))


# @lc code=end
