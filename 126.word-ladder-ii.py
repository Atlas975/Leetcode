#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
from itertools import product
from collections import OrderedDict, defaultdict, deque
from string import ascii_lowercase
from typing import List, Optional


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        word_set = set(wordList)
        res = []
        if endWord not in word_set:
            return []
        bq, eq = deque([(beginWord, [])]), deque([(endWord, [])])
        bpos, epos = {beginWord: [[beginWord]]}, {endWord: [[endWord]]}

        def directed_bfs(bq: deque, bpos: dict, epos: dict) -> Optional[List]:
            for w, path in (bq.popleft() for _ in range(len(bq))):
                for c, st, en in ((c, w[:i], w[i + 1 :]) for i, c in enumerate(w)):
                    for nw in (f"{st}{l}{en}" for l in ascii_lowercase if l != c):
                        if nw in epos:
                            return [path] + [epos[nw][::-1]]
                        if nw in word_set:
                            bpos[nw] = path + [nw]
                            bq.append((dist + 1, nw))
                            word_set.remove(nw)
            return None

        while bq and eq:
            if res := directed_bfs(bq, bpos, epos):
                return res
            if len(bq) > len(eq):
                bq, bpos, eq, epos = eq, epos, bq, bpos
        return []


# @lc code=end
