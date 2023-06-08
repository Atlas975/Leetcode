#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start

from collections import Counter
from itertools import chain, product


class TrieNode:
    def __init__(self):
        self.children = {}
        self.refcnt = 0
        self.is_word = False
        self.is_rev = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, rev):
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
            node.refcnt += 1
        node.is_word = True
        node.is_rev = rev

    def remove(self, word):
        node = self.root
        for i, c in enumerate(word):
            parent = node
            node = node.children[c]

            if node.refcnt == 1:
                path = [(parent, c)]
                for c in word[i + 1 :]:
                    path.append((node, c))
                    node = node.children[c]
                for parent, c in path:
                    parent.children.pop(c)
                return
            node.refcnt -= 1
        node.is_word = False


class Solution:
    def findWords(self, board, words) -> List[str]:
        res = []
        n, m = len(board), len(board[0])
        trie = Trie()

        boardcnt = Counter(chain(*board))
        for w, wrdcnt in ((w, Counter(w)) for w in words):
            if any(wrdcnt[c] > boardcnt[c] for c in wrdcnt): # word impossible to find
                continue
            if wrdcnt[w[0]] < wrdcnt[w[-1]]: 
                trie.insert(w, False)
            else: # word more likely to be found from end
                trie.insert(w[::-1], True)

        def dfs(r, c, parent) -> None:
            if not (node := parent.children.get(board[r][c])):
                return
            path.append(board[r][c])
            board[r][c] = "#"
            if node.is_word:
                word = "".join(path)
                res.append(word[::-1] if node.is_rev else word)
                trie.remove(word)

            dfs(r - 1, c, node) if r > 0 else None
            dfs(r + 1, c, node) if r < n - 1 else None
            dfs(r, c - 1, node) if c > 0 else None
            dfs(r, c + 1, node) if c < m - 1 else None
            board[r][c] = path.pop()

        path = []
        for r, c in product(range(n), range(m)):
            dfs(r, c, trie.root)
        return res

        # n, m = len(board), len(board[0])
        # dic = defaultdict(set)

        # for r, c in product(range(n), range(m)):
        #     dic[board[r][c]].add((r, c))

        # res = deque()

        # word, lngth, word_isReversed = "", 0, False

        # def dfs(cord, i):
        #     if i == lngth:
        #         res.append(word[::-1] if word_isReversed else word)
        #         return True

        #     ch = word[i]
        #     r, c = cord
        #     for cand in [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]:
        #         if cand in dic[ch]:
        #             dic[ch].remove(cand)
        #             flag = dfs(cand, i + 1)
        #             dic[ch].add(cand)
        #             if flag:
        #                 return True

        #     return False

        # ref = {board[n - 1][j] + board[n - 1][j + 1] for j in range(m - 1)}
        # ref.update(board[i][m - 1] + board[i + 1][m - 1] for i in range(n - 1))
        # for r, c in product(range(n - 1), range(m - 1)):
        #     ref.add(board[r][c] + board[r][c + 1])
        #     ref.add(board[r][c] + board[r + 1][c])

        # for w in words:
        #     if all(w[i] + w[i + 1] in ref or w[i + 1] + w[i] in ref for i in range(len(w) - 1)):
        #         if w[:4] == w[0] * 4 or len(dic[w[-1]]) < len(dic[w[0]]):
        #             word = w[::-1]
        #             word_isReversed = True
        #         else:
        #             word = w
        #             if word_isReversed:
        #                 word_isReversed = False

        #         lngth = len(word)
        #         for cord in list(dic[word[0]]):
        #             dic[word[0]].remove(cord)
        #             flag = dfs(cord, 1)
        #             dic[word[0]].add(cord)
        #             if flag:
        #                 break
        # return res


# @lc code=end
