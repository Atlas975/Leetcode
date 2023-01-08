#
# @lc app=leetcode id=2013 lang=python3
#
# [2013] Detect Squares
#

# @lc code=start
from collections import Counter


class DetectSquares:
    def __init__(self):
        self.pntcnt = Counter()

    def add(self, point: List[int]) -> None:
        self.pntcnt[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        return sum(
            freq2 * self.pntcnt[x2, y1] * self.pntcnt[x1, y2]
            for (x2, y2), freq2 in self.pntcnt.items()
            if abs(x2 - x1) == abs(y2 - y1)
        ) - (self.pntcnt[x1, y1] ** 3)


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end
