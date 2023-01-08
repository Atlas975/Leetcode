#
# @lc app=leetcode id=1705 lang=python3
#
# [1705] Maximum Number of Eaten Apples
#

# @lc code=start

import heapq as hq


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        stash = []
        res = 0

        def validapple(i, stash):  # check if apple exists
            while stash and (stash[0][0] <= i or stash[0][1] == 0):
                hq.heappop(stash)  # remove expired apples
            if stash:
                stash[0][1] -= 1
                return 1
            return 0

        for i, apple in enumerate(apples):
            if apple > 0:
                hq.heappush(stash, [i + days[i], apple])
            res += validapple(i, stash)

        i = len(apples)
        while stash:
            res += validapple(i, stash)
            i += 1

        return res


# @lc code=end
