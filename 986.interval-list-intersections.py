#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        res = []
        l1, l2 = len(firstList), len(secondList)
        i, j = 0, 0

        while i < l1 and j < l2:
            lmax = max(firstList[i][0], secondList[j][0])
            rmin = min(firstList[i][1], secondList[j][1])

            if lmax <= rmin:
                res.append([lmax, rmin])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return res


# @lc code=end
