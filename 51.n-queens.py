#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, pdiag, ndiag = set(), set(), set()
        res = []

        def dfs(r, path):
            for c in range(n):
                if (c in cols) or (r + c in pdiag) or (r - c in ndiag):
                    continue
                if r + 1 == n:
                    path.append(c)
                    res.append(("." * i + "Q" + "." * (n - i - 1)) for i in path)
                    return

                cols.add(c)
                pdiag.add(r + c)
                ndiag.add(r - c)
                dfs(r + 1, path + [c])
                cols.remove(c)
                pdiag.remove(r + c)
                ndiag.remove(r - c)

        dfs(0, [])
        return res


# @lc code=end
