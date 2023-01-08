#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import defaultdict


class Trie:
    def __init__(self):
        self.children: dict[str, Trie] = defaultdict(Trie)
        self.end: bool = False

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            if not curr.children.get(c):
                curr.children[c]
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if not curr.children.get(c):
                return False
            curr = curr.children[c]
        return curr.end

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
            trie = Trie()

            def dfs()
            for node in trie.children:



# @lc code=end

