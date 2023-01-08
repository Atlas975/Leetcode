#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, path):
            if not nums:
                res.append(path)
                return
            for i, cur in enumerate(nums):
                dfs(nums[:i] + nums[i + 1 :], path + [cur])

        dfs(nums, [])
        return res


# @lc code=end
