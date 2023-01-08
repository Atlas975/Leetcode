#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# @lc code=start


from collections import defaultdict


class Trie:
    def __init__(self):
        self.children: dict[str, Trie] = defaultdict(Trie)
        self.is_word: bool = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            node = node.children[c]
        node.is_word = True

    def remove(self, word: str) -> None:
        path = [self]
        for c in word:
            if not path[-1].children.get(c):
                return
            path.append(path[-1].children[c])

        if path[-1].is_word:
            return
        path[-1].is_word = False
        if len(path[-1].children) > 0:
            return

        remroot = word[-1]
        for node, c in zip(path[-2::-1], word[-2::-1]):
            if len(node.children) > 1 or node.is_word:
                del node.children[remroot]
                return
            remroot = c

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if not node.children.get(c):
                return False
            node = node.children[c]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            if not node.children.get(c):
                return False
            node = node.children[c]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("hello")
obj.insert("hell")
print(obj.search("hello"))
print(obj.startsWith("he"))
print(obj.remove("hell"))
print(obj.startsWith("hello"))
# param_3 = obj.startsWith(prefix)
# @lc code=end
