#
# @lc app=leetcode id=976 lang=python3
#
# [976] Largest Perimeter Triangle
#

# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        while len(nums) >= 3 and nums[-1] >= nums[-2] + nums[-3]:
            nums.pop()
        return sum(nums[-3:]) if len(nums) >= 3 else 0


# @lc code=end
