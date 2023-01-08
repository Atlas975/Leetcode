#
# @lc app=leetcode id=2248 lang=python3
#
# [2248] Intersection of Multiple Arrays
#

# @lc code=start


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return sorted(set.intersection(*map(set, nums)))


# @lc code=end
