#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n * m - 1

        while l < r:
            mid = l + (r - l) // 2
            mval = matrix[mid // m][mid % m]

            if mval < target:
                l = mid + 1
            elif mval > target:
                r = mid - 1
            else:
                return True

        return matrix[l // m][l % m] == target


# @lc code=end
