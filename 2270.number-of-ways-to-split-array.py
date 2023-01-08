#
# @lc app=leetcode id=2270 lang=python3
#
# [2270] Number of Ways to Split Array
#

# @lc code=start
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res = 0
        l_sum = 0
        r_sum = sum(nums)
        for num in nums[:-1]:
            l_sum += num
            r_sum -= num
            if l_sum >= r_sum:
                res += 1
        return res


# @lc code=end
