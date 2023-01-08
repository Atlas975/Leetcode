#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start

from collections import defaultdict


class WordDictionary:
    def __init__(self):
        self.wordsze = set()
        self.children = defaultdict(WordDictionary)
        self.is_word = False

    def addWord(self, word: str) -> None:
        self.wordsze.add(len(word))
        node = self
        for c in word:
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        n = len(word)

        def dfs(i, node):
            if i == n:
                return node.is_word
            if word[i] == ".":
                return any(dfs(i + 1, v) for v in node.children.values())
            if word[i] not in node.children:
                return False
            return dfs(i + 1, node.children[word[i]])

        return (n in self.wordsze) and dfs(0, self)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
