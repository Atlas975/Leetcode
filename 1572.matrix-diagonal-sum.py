#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        return sum(mat[i][i] + mat[i][n - i - 1] for i in range(n)) - (
            mat[n // 2][n // 2] if n % 2 else 0
        )


# @lc code=end
