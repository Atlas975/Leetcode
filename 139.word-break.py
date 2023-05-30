#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#


# @lc code=start

from collections import defaultdict, deque


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

def build_trie(wordDict):
    root = TrieNode()
    for word in wordDict:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
    return root
    
def search_trie(node, s):
    for char in s:
        if char not in node.children:
            return False
        node = node.children[char]
    return node.is_word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ns = len(s)
        dp = [False] * (ns + 1)
        dp[-1] = True

        wordmp = defaultdict(set)
        for w in wordDict:
            wordmp[len(w)].add(w)

        for i in reversed(range(ns)):
            for wlen in wordmp:
                if i + wlen > ns:
                    continue
                if s[i : i + wlen] in wordmp[wlen]:
                    dp[i] = dp[i + wlen]
                    if dp[i]:
                        break
        return dp[0]

        trie = build_trie(wordDict)
        q = deque([0])
        seen = set()

        while q:
            i = q.popleft()
            if i in seen:
                continue
            seen.add(i)
            node = trie

            for j in range(i, len(s)):
                char = s[j]
                if char not in node.children:
                    break
                node = node.children[char]
                if node.is_word:
                    if j + 1 == len(s):
                        return True
                    q.append(j + 1)

        return False


# @lc code=end
