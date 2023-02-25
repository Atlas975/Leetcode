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

        fmax = smax = 0
        for degree in degrees:
            if degree > fmax:
                fmax, smax = degree, fmax
            elif degree > smax:
                smax = degree

        fmcnt = smcnt = 0
        for degree in degrees:
            if degree == fmax:
                fmcnt += 1
            elif degree == smax:
                smcnt += 1

        if fmcnt >= 2:
            edgecnt = sum((degrees[u] == fmax and degrees[v] == fmax) for u, v in roads)
            return 2 * fmax - ((fmcnt * (fmcnt - 1) // 2) == edgecnt)

        edgecnt = sum(
            (degrees[u] == fmax and degrees[v] == smax) + (degrees[u] == smax and degrees[v] == fmax) for u, v in roads
        )
        return fmax + smax - (smcnt == edgecnt)


# @lc code=end
