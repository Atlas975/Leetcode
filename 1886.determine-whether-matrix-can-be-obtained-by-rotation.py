#
# @lc app=leetcode id=1886 lang=python3
#
# [1886] Determine Whether Matrix Can Be Obtained By Rotation
#

# @lc code=start
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            n = len(mat)
            for i in range(n // 2):
                for j in range(i, n - i - 1):
                    (mat[i][j], mat[j][n - i - 1], mat[n - i - 1][n - j - 1], mat[n - j - 1][i],) = (
                        mat[n - j - 1][i],
                        mat[i][j],
                        mat[j][n - i - 1],
                        mat[n - i - 1][n - j - 1],
                    )

        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)
        return False


# @lc code=end
