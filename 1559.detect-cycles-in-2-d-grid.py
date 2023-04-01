#
# @lc app=leetcode id=1559 lang=python3
#
# [1559] Detect Cycles in 2D Grid
#

# @lc code=start
from itertools import product


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]

        def dfs(r, c, prev=None):
            if visited[r][c]:
                return True
            visited[r][c] = True
            return any(
                n > dr >= 0
                and m > dc >= 0
                and grid[r][c] == grid[dr][dc]
                and (dr, dc) != prev
                and dfs(dr, dc, (r, c))
                for dr, dc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
            )

        return any(not visited[r][c] and dfs(r, c) for r, c in product(range(n), range(m)))


# @lc code=end
