#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # matrix[l][l + i] = top left
        # matrix[l + i][r] = top right
        # matrix[r][r - i] = bottom right
        # matrix[r - i][l] = bottom left

        l = 0
        r = len(matrix) - 1

        # 90 degree clockwise
        while l < r:
            for i in range(r - l):
                tleft = matrix[l][l + i]
                matrix[l][l + i] = matrix[r - i][l]
                matrix[r - i][l] = matrix[r][r - i]
                matrix[r][r - i] = matrix[l + i][r]
                matrix[l + i][r] = tleft
            r -= 1
            l += 1

        """
        # 90 degree counterclockwise
        while l<r:
            for i in range(r-l):
                tleft=matrix[l][l+i]
                matrix[l][l+i] = matrix[l+i][r]
                matrix[l+i][r] = matrix[r][r-i]
                matrix[r][r-i] = matrix[r-i][l]
                matrix[r-i][l] = tleft
            r-=1
            l+=1
        """

        """
        Do not return anything, modify matrix in-place instead.
        """


# @lc code=end
