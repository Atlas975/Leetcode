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

        def bfs(r, c, visited):
            visited.add((r, c))
            node = heights[r][c]
            for dr, dc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (
                    0 <= dr < n
                    and 0 <= dc < m
                    and (dr, dc) not in visited
                    and heights[dr][dc] >= node
                ):
                    bfs(dr, dc, visited)

        for r in range(n):
            bfs(r, 0, pac)
            bfs(r, m - 1, atc)
        for c in range(m):
            bfs(0, c, pac)
            bfs(n - 1, c, atc)
        return pac & atc


# @lc code=end
