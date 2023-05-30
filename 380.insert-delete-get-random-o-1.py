#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random


class RandomizedSet:
    def __init__(self):
        self.mp = {}
        self.s = []

    def insert(self, val: int) -> bool:
        if not_exists := val not in self.mp:
            self.mp[val] = len(self.s)
            self.s.append(val)
        return not_exists

    def remove(self, val: int) -> bool:
        if exists := val in self.mp:
            del_i, lst_v = self.mp[val], self.s[-1]
            self.mp[lst_v] = del_i # last gets the old index
            self.s[del_i] = lst_v
            self.s.pop()
            self.mp.pop(val)
        return exists

    def getRandom(self) -> int:
        return random.choice(self.s)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
