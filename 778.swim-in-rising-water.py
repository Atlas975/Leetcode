#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
from collections import deque
import heapq


class Solution:
    def swimInWater(self, grid) -> int:
        # BINARY SEARCH
        n = len(grid)
        l, r = grid[-1][-1], max(map(max, grid)) # min and max time

        def dfs(i, j, t, seen, outbound):
            if outbound or (grid[i][j] > t) or ((i, j) in seen):
                return False
            seen.add((i, j))

            if i == j == n - 1:
                return True
            return (
                dfs(i + 1, j, t, seen, i == n - 1)
                or dfs(i, j + 1, t, seen, j == n - 1)
                or dfs(i - 1, j, t, seen, i == 0)
                or dfs(i, j - 1, t, seen, j == 0)
            )

        while l < r:
            m = l + (r - l) // 2
            if dfs(0, 0, m, set(), False):
                r = m
            else:
                l = m + 1
        return l


        # DIJKSTRA ALGORITHM + BIDIRECTIONAL BFS
        n = len(grid)
        mxt = max(grid[0][0], grid[n - 1][n - 1])  # result will always be >= to this
        spq, dpq = [(mxt, 0, 0)], [(mxt, n - 1, n - 1)]  # pops lowest from src and dst
        spos, dpos = [[None] * n for _ in range(n)], [[None] * n for _ in range(n)]
        spos[0][0] = dpos[n - 1][n - 1] = mxt

        def bfs_exp(mxt, i, j, outbound):
            if outbound or spos[i][j]:
                return
            if grid[i][j] > mxt:
                spos[i][j] = grid[i][j]
                heapq.heappush(spq, (grid[i][j], i, j))
            else:
                spos[i][j] = mxt
                bfs.append((i, j))

        while spq and dpq:
            for t, i, j in (heapq.heappop(spq) for _ in range(len(spq))):
                mxt = t
                bfs = deque([(i, j)])
                while bfs:
                    nr, nc = bfs.popleft()
                    if emxt := dpos[nr][nc]:
                        return max(mxt, emxt)
                    bfs_exp(mxt, nr - 1, nc, nr == 0)
                    bfs_exp(mxt, nr + 1, nc, nr == n - 1)
                    bfs_exp(mxt, nr, nc - 1, nc == 0)
                    bfs_exp(mxt, nr, nc + 1, nc == n - 1)

            if len(spq) > len(dpq):  # swap to minimize BFS tree
                spq, spos, dpq, dpos = dpq, dpos, spq, spos
        return mxt


# @lc code=end
