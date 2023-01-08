#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total, lsum = sum(nums), 0

        for i, num in enumerate(nums):
            if lsum == (total - num) - lsum:
                return i
            lsum += num
        return -1


# @lc code=end
