#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start


from collections import deque


class WordDictionary:
    def __init__(self):
        self.triemp = {}  # len -> {char -> {char -> ...}}

    def addWord(self, word: str) -> None:
        node = self.triemp.setdefault(len(word), {})
        for c in word:
            node = node.setdefault(c, {})

    def search(self, word: str) -> bool:
        n = len(word)
        if not (trie := self.triemp.get(n)):
            return False
        s = deque([(0, trie)])
        
        while s:
            i, node = s.pop()
            if i == n:
                return True
            if (c := word[i]) == ".":
                s.extend((i + 1, v) for v in node.values())
            elif c in node:
                s.append((i + 1, node[c]))
        return False




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
