#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, ans, prefix = 0, n, 1

        for r in range(n):
            prefix *= nums[r]
            while l <= r and prefix >= k:
                prefix /= nums[l]
                l += 1
            ans += r - l
        return ans


# @lc code=end
