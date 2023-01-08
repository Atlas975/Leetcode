#
# @lc app=leetcode id=775 lang=python3
#
# [775] Global and Local Inversions
#

# @lc code=start
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            if i - num not in {-1, 0, 1}:
                return False
        return True


# @lc code=end
