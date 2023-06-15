#
# @lc app=leetcode id=1816 lang=python3
#
# [1816] Truncate Sentence
#


# @lc code=start
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res = []
        i, n = 0, len(s)
        for _ in range(k):
            j = i
            while j < n and s[j] != " ":
                j += 1
            res.append(s[i:j])
            i = j + 1
        return " ".join(res)


# @lc code=end
