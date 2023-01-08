#
# @lc app=leetcode id=1752 lang=python3
#
# [1752] Check if Array Is Sorted and Rotated
#

# @lc code=start
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        k = 0
        for i, num in enumerate(nums):
            if num > nums[(i + 1) % n]:
                k += 1
            if k > 1:
                return False
        return True


# @lc code=end
