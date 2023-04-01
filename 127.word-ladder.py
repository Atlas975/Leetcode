#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start


from collections import deque
from string import ascii_lowercase
from typing import List, Optional


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        bq, eq = deque([(1, beginWord)]), deque([(1, endWord)])
        bpos, epos = {beginWord: 1}, {endWord: 1}

        def bfs(bq: deque, bp: dict, ep: dict) -> Optional[int]:
            for bdist, w in (bq.popleft() for _ in range(len(bq))):
                for st, c, en in ((w[:i], c, w[i + 1 :]) for i, c in enumerate(w)):
                    for nw in (st + l + en for l in ascii_lowercase if l != c):
                        if edist := ep.get(nw):
                            return bdist + edist
                        if nw in word_set:
                            bp[nw] = bdist + 1
                            bq.append((bdist + 1, nw))
                            word_set.remove(nw)

        while bq and eq:
            if res := bfs(bq, bpos, epos) if len(bq) < len(eq) else bfs(eq, epos, bpos):
                return res
        return 0


# @lc code=end
