from collections import deque
from itertools import product


class Solution:
    def walls_and_gates(self, rooms: List[List[int]]):
        n, m = len(rooms), len(rooms[0])
        q = deque((r, c) for r, c in product(range(n), range(m)) if rooms[r][c] == 0)

        def expand(r, c, dist, valididx):
            if valididx and (dist + 1) < rooms[r][c]:
                rooms[r][c] = dist + 1
                q.append((r, c))

        while q:
            r, c = q.popleft()
            expand(r - 1, c, rooms[r][c], r > 0)
            expand(r + 1, c, rooms[r][c], r < n - 1)
            expand(r, c - 1, rooms[r][c], c > 0)
            expand(r, c + 1, rooms[r][c], c < m - 1)
        # write your code here
