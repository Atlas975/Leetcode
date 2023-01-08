#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        nums.sort()
        for i, num in enumerate(nums):
            if num == k:
                res += 1
            for j in range(i + 1, len(nums)):
                num += nums[j]
                if num == k:
                    res += 1
                    break
                elif num > k:
                    break
        return res


# @lc code=end
