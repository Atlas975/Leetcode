#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxsub = cursum = nums[0]

        for num in nums[1:]:
            cursum = (cursum + num) if cursum > 0 else num
            mxsub = max(mxsub, cursum)
        return mxsub


# @lc code=end
