#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
from itertools import product


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        col0 = any(matrix[i][0] == 0 for i in range(n))

        for r, c in product(range(n), range(1, m)):
            if matrix[r][c] == 0:
                matrix[r][0] = matrix[0][c] = 0

        for r, c in product(reversed(range(n)), range(1, m)):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

        if col0:
            for i in range(n):
                matrix[i][0] = 0


# @lc code=end
