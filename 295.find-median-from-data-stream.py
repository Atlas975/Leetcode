#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq as hq


class MedianFinder:
    def __init__(self):
        self.lmax, self.rmin = [], []
        self.iseven = 1

    def addNum(self, num: int) -> None:
        if self.iseven:
            hq.heappush(self.rmin, -hq.heappushpop(self.lmax, -num))
        else:
            hq.heappush(self.lmax, -hq.heappushpop(self.rmin, num))
        self.iseven ^= 1

    def findMedian(self) -> float:
        return (self.rmin[0] - self.lmax[0]) / 2 if self.iseven else self.rmin[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
