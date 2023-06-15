#
# @lc app=leetcode id=1776 lang=python3
#
# [1776] Car Fleet II
#


# @lc code=start
from collections import deque


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        res = [-1] * n
        stack = deque()

        for i in reversed(range(n)):
            p1, s1 = cars[i]
            while stack and s1 <= stack[-1][1]: # can't catch up
                stack.pop()
            while stack: # 
                p2, s2, j = stack[-1]
                collideTime = (p2 - p1) / (s1 - s2)
                if res[j] == -1 or collideTime <= res[j]: # earlier collision
                    res[i] = collideTime
                    break   
                stack.pop()
            stack.append((p1, s1, i))
        return res


                


# @lc code=end
