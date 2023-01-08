#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start

from itertools import count, takewhile


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mxlen = 0
        dp = set(nums)
        for num in dp:
            if (num - 1) not in dp:
                size = 1
                while (num + size) in dp:
                    size += 1
                mxlen = max(mxlen, size)
        return mxlen


# @lc code=end
