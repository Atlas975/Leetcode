#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {c: i for i, c in enumerate(order)}
        lexmap = lambda word: [order_dict[c] for c in word]

        prev = lexmap(words[0])
        return all(prev <= (prev := lexmap(word)) for word in words[1:])

        # words=[[order_dict[c] for c in word] for word in words]
        # return all(w1<=w2 for w1,w2 in zip(words,words[1:]))


# @lc code=end
