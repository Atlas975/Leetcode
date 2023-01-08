#
# @lc app=leetcode id=2024 lang=python3
#
# [2024] Maximize the Confusion of an Exam
#

# @lc code=start
from collections import defaultdict


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        freq = defaultdict(int)
        longest, maxf, l = 0, 0, 0
        for r, c in enumerate(answerKey):
            freq[c] += 1
            maxf = max(maxf, freq[c])
            if r - l + 1 - maxf > k:
                freq[answerKey[l]] -= 1
                l += 1
            else:
                longest = max(longest, r - l + 1)
        return longest


# @lc code=end
