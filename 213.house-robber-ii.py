#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_group(start, end):
            a, b = 0, 0
            for num in nums[start:end]:
                a, b = b, max(a + num, b)
            return b

        n = len(nums)
        if n < 2:
            return nums[0]
        return max(rob_group(0, n - 1), rob_group(1, n))


# @lc code=end
