#
# @lc app=leetcode id=1129 lang=python3
#
# [1129] Shortest Path with Alternating Colors
#

# @lc code=start
class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        res = [float("inf")] * n


# @lc code=end
