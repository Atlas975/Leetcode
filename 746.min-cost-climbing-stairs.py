#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]
        for c in cost[2:]:
            a, b = b, min(a, b) + c
        return min(a, b)


# @lc code=end
