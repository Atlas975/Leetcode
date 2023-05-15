#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, path):
            if i == n:
                res.append(path.copy())
                return

            path.append(nums[i])
            dfs(i + 1, path) # permute with nums[i]
            path.pop()

            while i < n - 1 and nums[i] == nums[i + 1]: 
                i += 1
            dfs(i + 1, path) # permute without nums[i] (skip duplicates)

        nums.sort()
        n = len(nums)
        dfs(0, [])
        return res


# @lc code=end
