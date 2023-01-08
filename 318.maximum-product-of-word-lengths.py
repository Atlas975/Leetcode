#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
from collections import defaultdict
from itertools import combinations


class Solution:
    def maxProduct(self, words: List[str]) -> int:

        wordset = defaultdict(int)
        for word in words:
            for letter in word:
                wordset[word] |= 1 << (ord(letter) - 97)

        res = 0
        for w1, w2 in combinations(words, 2):
            if len(w1) * len(w2) > res and wordset[w1] & wordset[w2] == 0:
                res = len(w1) * len(w2)

        return res


# @lc code=end
