#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, numRows):
            prev = res[i - 1]
            for j in range(1, i):
                res[i][j] = prev[j - 1] + prev[j]
        return res


# @lc code=end
