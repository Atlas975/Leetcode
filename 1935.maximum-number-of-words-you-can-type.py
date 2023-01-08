#
# @lc app=leetcode id=1935 lang=python3
#
# [1935] Maximum Number of Words You Can Type
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        b = set(brokenLetters)
        return sum(not b & w for w in map(set, text.split()))


# @lc code=end
