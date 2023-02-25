#
# @lc app=leetcode id=1594 lang=python3
#
# [1594] Maximum Non Negative Product in a Matrix
#

# @lc code=start


from functools import cache


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        @cache
        def dfs(r, c, val):
            val *= grid[r][c]
            if r == n - 1 and c == m - 1:
                return val
            return max(dfs(dr, dc, val) for dr, dc in ((r, c + 1), (r + 1, c)) if (0 <= dr < n and 0 <= dc < m))

        res = dfs(0, 0, 1)
        return -1 if res < 0 else res % (10**9 + 7)


# @lc code=end
