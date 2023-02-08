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
        self.f_k_v = defaultdict(OrderedDict)
        self.k_f = {}
        self.minf = 1

    def update(self, key: int, freq: int, new_val: int) -> None:
        self.f_k_v[freq + 1][key] = new_val
        self.k_f[key] = freq + 1

        if self.f_k_v[freq]:
            return
        del self.f_k_v[freq]
        if self.minf == freq:
            self.minf += 1

    def get(self, key: int) -> int:
        if freq := self.k_f.get(key):
            value = self.f_k_v[freq].pop(key)
            self.update(key, freq, value)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if freq := self.k_f.get(key):
            self.f_k_v[freq].pop(key)
            self.update(key, freq, value)
            return

        self.k_f[key] = 1
        self.f_k_v[1][key] = value
        if len(self.k_f) > self.cap:
            fifo_k = self.f_k_v[self.minf].popitem(last=False)[0]
            del self.k_f[fifo_k]
        self.minf = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
