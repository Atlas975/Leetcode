#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(r, path, cols, pdiag, ndiag):
            for c in range(n):
                if (cols & (1 << c)) or (pdiag & (1 << (r + c))) or (ndiag & (1 << (r - c + n))):
                    continue

                if r == n - 1:
                    path.append(c)
                    res.append("." * c + "Q" + "." * (n - c - 1) for c in path)
                    return

                dfs(
                    r + 1,
                    path + [c],
                    cols | 1 << c,
                    pdiag | 1 << (r + c),
                    ndiag | 1 << (r - c + n),
                )

        dfs(0, [], 0, 0, 0)
        return res


# @lc code=end
