#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#


# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        pac, atc = set(), set()

        def bfs(r, c, ocean):
            ocean.add((r, c))
            for nr, nc, outbound in (
                (r - 1, c, r == 0),
                (r + 1, c, r == n - 1),
                (r, c - 1, c == 0),
                (r, c + 1, c == m - 1),
            ):
                if outbound or heights[nr][nc] < heights[r][c] or (nr, nc) in ocean:
                    continue
                bfs(nr, nc, ocean)

        for r in range(n):
            bfs(r, 0, pac)
            bfs(r, m - 1, atc)
        for c in range(m):
            bfs(0, c, pac)
            bfs(n - 1, c, atc)
        return pac & atc


# @lc code=end