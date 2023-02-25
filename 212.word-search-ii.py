#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start

# I haven't learned Trie yet. This solutions comes from Discussion section.
from collections import defaultdict, deque
from itertools import chain, product


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


class Solution:
    def findWords(self, board, words) -> List[str]:
        res = []
        n, m = len(board), len(board[0])
        root = Trie()
        for word in words:
            root.insert(word)

        def bfs(word: str, node: Trie, r: int, c: int) -> None:
            if node.is_word:
                res.append(word)
                root.remove(word)

            board[r][c] = "#"

            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < n and 0 <= nc < m and (nex := node.children.get(board[nr][nc])):
                    bfs(word + board[nr][nc], nex, nr, nc)

            board[r][c] = word[-1]

        for r, c in product(range(n), range(m)):
            if node := root.children.get(board[r][c]):
                bfs(board[r][c], node, r, c)
        return res


# @lc code=end
