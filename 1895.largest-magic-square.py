#
# @lc app=leetcode id=1895 lang=python3
#
# [1895] Largest Magic Square
#

# @lc code=start
from itertools import product


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        mxsize = min(n, m)  # max size of magic square

        for k in range(mxsize, 1, -1):
            for r, c in product(range(n - k + 1), range(m - k + 1)):
                if self.valid_square(r, c, k, grid):
                    return k
        return 1

    def valid_square(self, r, c, k, grid):

        sums = {
            sum((grid[r + i][c + i] for i in range(k))),  # diagonal
            sum((grid[r + i][c + k - i - 1] for i in range(k))),  # anti-diagonal
        }

        if len(sums) > 1:
            return False

        for i in range(k):
            sums.add(sum(grid[r + i][c + j] for j in range(k)))  # col sum
            if len(sums) > 1:
                return False
            sums.add(sum(grid[r + j][c + i] for j in range(k)))  # row sum
            if len(sums) > 1:
                return False

        return True


# @lc code=end
