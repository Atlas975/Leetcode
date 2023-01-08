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

        def expand(r, c):
            if grid[r][c] == 1:
                grid[r][c] = 2
                q.append((r, c))
                return 1
            return 0

        while fresh and q:
            qlen = len(q)
            for _ in range(qlen):
                r, c = q.popleft()
                fresh -= sum(
                    (
                        expand(r + 1, c) if r < n - 1 else 0,
                        expand(r - 1, c) if r > 0 else 0,
                        expand(r, c + 1) if c < m - 1 else 0,
                        expand(r, c - 1) if c > 0 else 0,
                    )
                )
            time += 1
        return -1 if fresh else time


# @lc code=end
