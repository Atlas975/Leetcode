#
# @lc app=leetcode id=2070 lang=python3
#
# [2070] Most Beautiful Item for Each Query
#

# @lc code=start
from collections import defaultdict


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        itemmp = defaultdict(int)
        itemmp = {}
        for item in items:
            itemmp[item[0]] = max(itemmp[item[0]], item[1])
        items = sorted(itemmp.items(), key=lambda x: x[1])


# @lc code=end
