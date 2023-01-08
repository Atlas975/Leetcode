#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
from collections import deque
import random


class RandomizedSet:
    def __init__(self):
        self.mp = {}
        self.s = deque()

    def insert(self, val: int) -> bool:
        not_exists = val not in self.mp
        if not_exists:
            self.mp[val] = len(self.s)
            self.s.append(val)
        return not_exists

    def remove(self, val: int) -> bool:
        exists = val in self.mp
        if exists:
            self.mp[self.s[-1]] = self.mp[val]
            self.s[self.mp[val]] = self.s[-1]
            self.s.pop()
            del self.mp[val]
        return exists

    def getRandom(self) -> int:
        return random.choice(self.s)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
