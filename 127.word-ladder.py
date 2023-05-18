#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start


from collections import deque
from string import ascii_lowercase


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        bq, eq = deque([(1, beginWord)]), deque([(1, endWord)])
        bpos, epos = {beginWord: 1}, {endWord: 1}

        while bq and eq:
            for bdist, st, c, en in (
                (bdist, w[:i], c, w[i + 1 :])
                for bdist, w in (bq.popleft() for _ in range(len(bq)))
                for i, c in enumerate(w)
            ):
                for nw in (f"{st}{l}{en}" for l in ascii_lowercase if l != c):
                    if edist := epos.get(nw):  # BFS from both ends converge
                        return bdist + edist
                    if nw in wordSet:
                        bpos[nw] = bdist + 1
                        bq.append((bdist + 1, nw))
                        wordSet.remove(nw)
            if len(bq) > len(eq):  # swap to minimize BFS tree
                bq, bpos, eq, epos = eq, epos, bq, bpos
        return 0


# @lc code=end
