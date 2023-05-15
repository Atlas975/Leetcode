#
# @lc app=leetcode id=2332 lang=python3
#
# [2332] The Latest Time to Catch a Bus
#

# @lc code=start
from itertools import takewhile


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        passengers.sort()
        n, m = len(buses), len(passengers)
        i = j = 0
        res = 0
        for b in sorted(buses):
            p, cnt = 0, 0
            for _ in takewhile(lambda p: p <= b, passengers[i:]):
                p += 1
                i += 1
                if p == capacity:
                    break


# @lc code=end
