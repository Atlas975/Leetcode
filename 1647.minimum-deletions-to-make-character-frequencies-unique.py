#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#

# @lc code=start

from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        if not s or len(s) == 1:
            return 0
        let_count = Counter(s)
        res = 0
        checked = set()
        for freq in let_count.values():
            while freq > 0 and freq in checked:
                freq -= 1
                res += 1
            checked.add(freq)
        return res


# @lc code=end
