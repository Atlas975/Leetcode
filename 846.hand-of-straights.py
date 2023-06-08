#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
from collections import Counter
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        crdcnt = Counter(hand)
        keypq = list(crdcnt.keys())
        heapq.heapify(keypq)

        while keypq:
            strt = keypq[0]
            for i in range(strt, strt + groupSize):
                if i not in crdcnt:
                    return False
                crdcnt[i] -= 1
                if crdcnt[i] == 0:
                    if i != keypq[0]:  # not at top of heap, hole in other group
                        return False
                    heapq.heappop(keypq)
        return True


# @lc code=end
