#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass(slots=True)
class Trie:
    children: dict = field(default_factory=lambda: defaultdict(Trie))
    refs: int = 0
    end: bool = False

    def insert(self, word: str) -> None:
        curr = self
        curr.refs += 1
        for c in word:
            if c not in curr.children:
                curr.children[c]
            curr = curr.children[c]
            curr.refs += 1
        curr.end = True

    def remove(self, word: str) -> None:
        curr = self
        curr.refs -= 1
        for c in word:
            if c not in curr.children:
                return
            curr = curr.children[c]
            curr.refs -= 1
        curr.end = False

    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        trie = Trie()
        for t in times:
            trie.insert(t)


# @lc code=end
