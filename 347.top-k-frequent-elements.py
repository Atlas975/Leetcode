#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in nums]
        for num, count in Counter(nums).items():
            freq[count - 1].append(num)

        res = []
        for f in freq[::-1]:
            for num in f:
                res.append(num)
                if len(res) == k:
                    return res


# @lc code=end
