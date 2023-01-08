#
# @lc app=leetcode id=2200 lang=python3
#
# [2200] Find All K-Distant Indices in an Array
#

# @lc code=start
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        l = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if num == key:
                res.extend(range(max(l, i - k), min(i + k + 1, n)))
                l = i + k + 1
        return res


# @lc code=end
