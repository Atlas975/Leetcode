#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        nr, nc = len(matrix), len(matrix[0])
        l, r = 0, nr * nc - 1

        while l <= r:
            m = l + (r - l) // 2
            mval = matrix[m // nc][m % nc]

            if mval < target:
                l = m + 1
            elif mval > target:
                r = m - 1
            else:
                return True
        return False


# @lc code=end
