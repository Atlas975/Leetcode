#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#


# @lc code=start
from collections import deque
from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        
        # ITERATIVE
        res = 0
        q = deque([(0, 0)])
        seen = set()

        while q:
            for i, j in (q.popleft() for _ in range(len(q))):
                if (i, j) in seen:
                    continue
                seen.add((i, j))
                while i < n1 and j < n2 and word1[i] == word2[j]:
                    i += 1
                    j += 1
                if i == n1 and j == n2:
                    return res
                q.extend([(i + 1, j), (i, j + 1), (i + 1, j + 1)])
            res += 1
        return res

        # RECURSIVE
        @cache
        def dfs(i, j):  # i, j are idx of start, target
            if i == n1:
                return n2 - j  # number of insertions needed
            if j == n2:
                return n1 - i  # number of deletions needed
            if word1[i] == word2[j]:  # no operation needed
                return dfs(i + 1, j + 1)
            insr, dele, repl = dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1)
            return 1 + min(insr, dele, repl)
        return dfs(0, 0)




# @lc code=end
