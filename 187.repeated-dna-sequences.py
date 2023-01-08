#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start


from collections import Counter


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        return (
            k
            for k, v in Counter((s[i : i + 10] for i in range(len(s) - 9))).items()
            if v > 1
        )


# @lc code=end
