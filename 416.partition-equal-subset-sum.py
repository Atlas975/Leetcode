#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
from functools import cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i, cursum) -> bool:
            if cursum == target:
                return True
            if cursum > target or i == 0:
                return False
            return dfs(i - 1, cursum + nums[i]) or dfs(i - 1, cursum)
        
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        nums.sort() # adding largest nums first speeds up dfs
        return dfs(len(nums) - 1, 0)


# @lc code=end
