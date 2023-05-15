#
# @lc app=leetcode id=1615 lang=python3
#
# [1615] Maximal Network Rank
#


# @lc code=start
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        for u, v in roads:
            degrees[u] += 1
            degrees[v] += 1

        mx1 = mx2 = mx2cnt = mx1cnt = 0
        for degree in degrees:
            if degree > mx1:
                mx1, mx2 = degree, mx1
                mx1cnt, mx2cnt = 1, mx1cnt
            elif degree == mx1:
                mx1cnt += 1
            elif degree > mx2:
                mx2 = degree
                mx2cnt = 1
            elif degree == mx2:
                mx2cnt += 1

        if mx1cnt > 1:
            edgecnt = sum((degrees[u] == mx1 and degrees[v] == mx1) for u, v in roads)
            return 2 * mx1 - ((mx1cnt * (mx1cnt - 1) // 2) == edgecnt)

        edgecnt = sum(
            (degrees[u] == mx1 and degrees[v] == mx2) + (degrees[u] == mx2 and degrees[v] == mx1) for u, v in roads
        )
        return mx1 + mx2 - (mx2cnt == edgecnt)


# @lc code=end
