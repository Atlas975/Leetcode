#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        for i in reversed(range(n - 1)):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


# @lc code=end
