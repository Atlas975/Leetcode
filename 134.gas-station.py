#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(cost) > sum(gas): # can't make a round trip
            return -1
        l = tank = 0

        for r, (co, ga) in enumerate(zip(cost, gas)):
            tank += ga - co
            if tank < 0: # gas is needed from earlier stations
                tank = 0
                l = r + 1
        return l


# @lc code=end
