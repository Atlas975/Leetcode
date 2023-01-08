#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
from collections import deque


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, n = deque(), len(nums)

        def dfs(i, path):
            if i == n:
                res.append(path.copy())
                return

            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, path)

        dfs(0, [])
        return res


# @lc code=end
