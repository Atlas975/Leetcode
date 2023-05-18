#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#


# @lc code=start
class Solution:
    def find_cheapest_price(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distmp = {dst: float("inf") for _, dst, cost in flights}
        distmp[src] = 0
        pq = [(0, src)]

        

        return -1


# @lc code=end
