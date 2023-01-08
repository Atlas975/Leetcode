#
# @lc app=leetcode id=1727 lang=python3
#
# [1727] Largest Submatrix With Rearrangements
#

# @lc code=start


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        height = [0] * m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    height[j] = 0
                else:
                    height[j] += 1
            colsums[sum(matrix[i][j] for j in range(m))] += 1

        width = m
        mxsize = -1
        # print(n, m, width)
        print(colsums)
        for i, cnt in enumerate(colsums):
            mxsize = max(mxsize, i * width)
            width -= cnt
        return mxsize

        # return max(
        #     (i+1)*colsums[i]*s
        #     for i in range(m)
        # )


# @lc code=end
