#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
from collections import Counter, defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = None

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]

    def get_word(self):
        return self.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)


# @lc code=end
