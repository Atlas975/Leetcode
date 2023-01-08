#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#
# @lc code=start
from functools import reduce


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        res = []
        for i in range(m * n):
            if i % c == 0:
                res.append([])
            res[-1].append(mat[i // n][i % n])
        return res


# @lc code=end
