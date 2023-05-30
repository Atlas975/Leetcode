#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crsMp = [[] for _ in range(numCourses)]
        needCnt = [0] * numCourses

        for crs, pre in prerequisites:
            crsMp[pre].append(crs)
            needCnt[crs] += 1

        q = deque([i for i in range(numCourses) if needCnt[i] == 0]) # no preq
        res = []

        while q:
            pre = q.popleft()
            res.append(pre)
            for crs in crsMp[pre]:
                needCnt[crs] -= 1
                if needCnt[crs] == 0: # no more preq
                    q.append(crs)
        return res if len(res) == numCourses else []


# @lc code=end
