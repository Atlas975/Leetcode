#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = set()
        for i in nums:
            if i in cache:
                return True
            cache.add(i)
        return False


# @lc code=end
