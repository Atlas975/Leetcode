#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#

# @lc code=start


from collections import OrderedDict, defaultdict


class Node:
    def __init__(self, key=0, value=0, pre=None, nex=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.nex = nex


class LRUCache:
    def __init__(self):
        self.cache = {}
        self.left, self.right = Node(), Node()
        self.left.nex, self.right.pre = self.right, self.left

    def _append(self, node: Node) -> None:
        l, r = self.right.pre, self.right
        node.pre, node.nex = l, r
        l.nex = r.pre = node
        self.cache[node.key] = node

    def _pop(self, key: int) -> Node:
        node = self.cache.pop(key)
        l, r = node.pre, node.nex
        l.nex, r.pre = r, l
        return node

    def popitem(self, key: int) -> tuple[int, int]:
        delnode = self._pop(key)
        return delnode.key, delnode.value

    def popleft(self) -> tuple[int, int]:
        return self.popitem(self.left.nex.key)

    def __setitem__(self, key: int, value: int) -> None:
        if node := self.cache.get(key):
            node.value = value
            self._append(self._pop(key))
            return
        self._append(Node(key, value))

    def __bool__(self) -> bool:
        return bool(self.cache)


class LFUCache:
    def __init__(self, cap: int):
        self.cap = cap
        self.f_k_v = defaultdict(OrderedDict)
        self.k_f = {}
        self.minf = 1

    def get(self, key: int) -> int:
        if not (freq := self.k_f.get(key)):
            return -1

        value = self.f_k_v[freq].pop(key)
        self.f_k_v[freq + 1][key] = value
        self.k_f[key] = freq + 1

        if not self.f_k_v[freq]:
            del self.f_k_v[freq]
            if self.minf == freq:
                self.minf += 1
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.k_f:
            self.get(key)
            self.f_k_v[self.k_f[key]][key] = value
            return

        self.cap -= 1
        self.k_f[key] = 1
        self.f_k_v[1][key] = value

        if self.cap < 0:
            fifo_k = self.f_k_v[self.minf].popitem(last=False)[0]
            del self.k_f[fifo_k]
            self.cap += 1
        self.minf = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
