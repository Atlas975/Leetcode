#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(arr, subset):
            res.append(subset)
            for i, num in enumerate(arr):
                dfs(arr[i + 1 :], subset + [num])

        dfs(nums, [])
        return res


# @lc code=end
