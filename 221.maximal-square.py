
#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
from itertools import product


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        def square_expand(i, j, k):
            for x in range(i, i+k):
                for y in range(j, j+k):
                    if matrix[x][y] == '0':
                        return False
            return True


        n, m = len(matrix), len(matrix[0])
        for r,c in product(range(n), range(m)):
            if m
# @lc code=end

 