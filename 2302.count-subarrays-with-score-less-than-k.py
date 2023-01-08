#
# @lc app=leetcode id=2302 lang=python3
#
# [2302] Count Subarrays With Score Less Than K
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        j = 0
        subsum = 0
        for i, num in enumerate(nums):
            subsum += num
            while subsum * (i - j + 1) >= k:
                subsum -= nums[j]
                j += 1
            res += i - j + 1
        return res


# @lc code=end
