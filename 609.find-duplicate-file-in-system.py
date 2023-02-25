#
# @lc app=leetcode id=609 lang=python3
#
# [609] Find Duplicate File in System
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dupes = defaultdict(list)
        for p in paths:
            direct, *files = p.split()
            for f in files:
                name, content = f.split("(", 1)
                dupes[content[:-1]].append(f"{direct}/{name}")
        return (dupe for dupe in dupes.values() if len(dupe) > 1)


# @lc code=end
