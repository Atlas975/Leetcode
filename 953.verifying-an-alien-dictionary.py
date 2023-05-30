#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#


# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordmp = {c: i for i, c in enumerate(order)}
        def isOrdered(w1, w2) -> bool:
            for a, b in ((ordmp[c1], ordmp[c2]) for c1, c2 in zip(w1, w2)):
                if a < b:
                    return True
                if a > b:
                    return False
            return len(w1) <= len(w2)
        return all(isOrdered(words[i - 1], words[i]) for i in range(1, len(words)))



# @lc code=end
