#
# @lc app=leetcode id=2404 lang=python3
#
# [2404] Most Frequent Even Element
#

# @lc code=start
from collections import Counter, defaultdict


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        res = Counter(num for num in nums if num % 2 == 0)
        if not res:
            return -1

        freqs = defaultdict(list)
        for num, freq in res.items():
            freqs[freq].append(num)

        return min(freqs[max(freqs.keys())])


# @lc code=end
