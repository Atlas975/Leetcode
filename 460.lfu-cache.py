#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#

# @lc code=start
from collections import OrderedDict, defaultdict


class LFUCache:
    def __init__(self, cap: int):
        self.cap = cap
        self.fkv = defaultdict(OrderedDict)
        self.kf = {}
        self.minf = 1

    def update(self, key: int, freq: int, new_val: int) -> None:
        self.fkv[freq + 1][key] = new_val
        self.kf[key] = freq + 1

        if self.fkv[freq]:
            return
        del self.fkv[freq]
        if self.minf == freq:
            self.minf += 1

    def get(self, key: int) -> int:
        if freq := self.kf.get(key):
            value = self.fkv[freq].pop(key)
            self.update(key, freq, value)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if freq := self.kf.get(key):
            self.fkv[freq].pop(key)
            self.update(key, freq, value)
            return

        self.kf[key] = 1
        self.fkv[1][key] = value
        if len(self.kf) > self.cap:
            fifo_k = self.fkv[self.minf].popitem(last=False)[0]
            del self.kf[fifo_k]
        self.minf = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
