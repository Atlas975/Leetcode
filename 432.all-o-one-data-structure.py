#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#

# @lc code=start
from collections import defaultdict


class AllOne:

    def __init__(self):
        self.smap = defaultdict(int)
        self.minhp = []
        self.maxhp = []


    def inc(self, key: str) -> None:
        self.smap[key] += 1


    def dec(self, key: str) -> None:
        self.smap[key] -= 1
        if self.smap[key] == 0:
            del self.smap[key]


    def getMaxKey(self) -> str:


    def getMinKey(self) -> str:



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end

