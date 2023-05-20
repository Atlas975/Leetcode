#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(arr, sub) -> List[List[int]]:
            subsets = [sub]
            for i, num in enumerate(arr):
                subsets.extend(dfs(arr[i + 1 :], sub + [num]))
            return subsets
        return dfs(nums, [])


# @lc code=end
