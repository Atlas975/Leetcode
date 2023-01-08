#
# @lc app=leetcode id=1267 lang=python3
#
# [1267] Count Servers that Communicate
#

# @lc code=start
from itertools import product


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        def bfs(r, c):
            total = 0
            for ci in range(m):
                if grid[r][ci] == 1:
                    grid[r][ci] = 0
                    total += 1
            for ri in range(n):
                if grid[ri][c] == 1:
                    grid[ri][c] = 0
                    total += 1
            return total - 1

        n, m = len(grid), len(grid[0])
        res = 0
        for r, c in product(range(n), range(m)):
            if grid[r][c] == 1:
                grid[r][c] = 0
                res += bfs(r, c)
        return res


# @lc code=end
