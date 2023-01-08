#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # n = len(gas)
        # for i in range(n):
        #     if tank := gas[i] - cost[i]:
        #         j = (i + 1) % n
        #         while j != i:
        #             tank += gas[j] - cost[j]
        #             if tank < 0:
        #                 break
        #             j = (j + 1) % n
        #         if j == i:
        #             return i + 1
        # return -1
        n = len(gas)
        l, r = 0, n - 1
        tank = gas[l] - cost[l]

        while l <= r:
            while tank < 0 and l <= r:
                l += 1
                tank -= gas[l] - cost[l]
            if l == r:
                return l
            tank += gas[r] - cost[r]
            r = (r - 1) % n

        return -1


# @lc code=end
