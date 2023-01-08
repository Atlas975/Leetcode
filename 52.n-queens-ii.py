#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, pdiag, ndiag = set(), set(), set()

        def bfs(r):
            comb = 0
            for c in range(n):
                if (c in cols) or (r + c in pdiag) or (r - c in ndiag):
                    continue
                if r + 1 == n:
                    return 1

                cols.add(c)
                pdiag.add(r + c)
                ndiag.add(r - c)
                comb += bfs(r + 1)
                cols.remove(c)
                pdiag.remove(r + c)
                ndiag.remove(r - c)
            return comb

        return bfs(0)


# @lc code=end
