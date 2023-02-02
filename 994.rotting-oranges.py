#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque
from itertools import product


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()
        fresh = time = 0

        for r, c in product(range(n), range(m)):
            if grid[r][c] == 1:
                fresh += 1
            elif grid[r][c] == 2:
                q.append((r, c))

        def expand(valid, r, c):
            if not valid or grid[r][c] != 1:
                return 0
            grid[r][c] = 2
            q.append((r, c))
            return 1

        while fresh and q:
            qlen = len(q)
            for _ in range(qlen):
                r, c = q.popleft()
                fresh -= (
                    expand(r < n - 1, r + 1, c)
                    + expand(r > 0, r - 1, c)
                    + expand(c < m - 1, r, c + 1)
                    + expand(c > 0, r, c - 1)
                )
            time += 1
            
        return -1 if fresh else time


# @lc code=end
