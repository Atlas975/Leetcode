#
# @lc app=leetcode id=1498 lang=python3
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#

# @lc code=start
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += 2 ** (r - l)
                l += 1
        return res % (10**9 + 7)


# @lc code=end
