#
# @lc app=leetcode id=2013 lang=python3
#
# [2013] Detect Squares
#

# @lc code=start
from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.xtoymp = defaultdict(lambda: defaultdict(int))
        self.ytoxmp = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xtoymp[x][y] += 1
        self.ytoxmp[y][x] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point
        horiz, verti1 = self.ytoxmp[y1], self.xtoymp[x1]

        for x2, p2f in horiz.items():  # points 1.origin 2.diffH 3.diffV 4.diffH/V 
            dif = x1 - x2  # side length
            verti2 = self.xtoymp[x2]

            if (p3f := verti1[y1 - dif]) and (p4f := verti2[y1 - dif]):
                res += p2f * p3f * p4f
            if (p3f := verti1[y1 + dif]) and (p4f := verti2[y1 + dif]):
                res += p2f * p3f * p4f
        return res - (2 * horiz[x1] ** 3)  # remove the origin point from res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end
