#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
from collections import deque


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        p1, s1 = pairs[0]
        stack = deque([(p1, (target - p1) / s1)])

        for p, s in pairs[1:]:
            t = (target - p) / s
            if t > stack[-1][1]:
                stack.append((p, t))
        return len(stack)


# @lc code=end
