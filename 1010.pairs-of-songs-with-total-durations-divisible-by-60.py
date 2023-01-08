#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#

# @lc code=start

from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = defaultdict(int)
        ans = 0

        for t in time:
            ans += cnt[-t % 60]
            cnt[t % 60] += 1

        return ans


# @lc code=end
