#
# @lc app=leetcode id=1582 lang=python3
#
# [1582] Special Positions in a Binary Matrix
#

# @lc code=start


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # def isOne(c):
        #     summ=0
        #     for i in range(0,len(mat)):
        #         summ+=mat[i][c]
        #     return summ==1

        isOne = lambda c: sum(mat[i][c] for i in range(len(mat))) == 1
        return sum(1 for row in mat if sum(row) == 1 and isOne(row.index(1)))

        # for row in mat:
        #     if sum(row) == 1 and isOne(row.index(1)):
        #         res += 1
        # return res


# @lc code=end
