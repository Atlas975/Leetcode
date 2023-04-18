#
# @lc app=leetcode id=2600 lang=python3
#
# [2600] K Items With the Maximum Sum
#


# @lc code=start
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes >= k:
            return k
        if numZeros >= k - numOnes:
            return numOnes
        return (2 * numOnes) - k + numZeros


# @lc code=end
