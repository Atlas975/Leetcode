#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start

from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsMp = [[] for _ in range(numCourses)]
        needCnt = [0] * numCourses

        for crs, pre in prerequisites:
            crsMp[pre].append(crs)
            needCnt[crs] += 1

        q = deque([i for i in range(numCourses) if needCnt[i] == 0])  # no preq
        valid = 0

        while q:
            pre = q.popleft()
            valid += 1
            for crs in crsMp[pre]:
                needCnt[crs] -= 1
                if needCnt[crs] == 0:
                    q.append(crs)
        return valid == numCourses


# @lc code=end
