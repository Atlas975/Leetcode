#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#

# @lc code=start


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        nums.sort()
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                res += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
        return res


# @lc code=end
