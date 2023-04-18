#
# @lc app=leetcode id=2596 lang=python3
#
# [2596] Check Knight Tour Configuration
#


# @lc code=start


from collections import ChainMap


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        if n <= 3: #* middle cell unreachable
            return False
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        x = y = 0

        for i in range(n * n):
            if grid[x][y] != i:
                return False
            for dy, dx in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == i + 1:
                    x, y = nx, ny
                    break
        return True


# @lc code=end
