#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start


class Node:
    def __init__(self, key=0, value=0, pre=None, nex=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.nex = nex


class LRUCache:
    def __init__(self, cap: int):
        self.cap = cap
        self.cache = {}
        self.left, self.right = Node(), Node()
        self.left.nex, self.right.pre = self.right, self.left

    def append(self, node: Node) -> None:
        l, r = self.right.pre, self.right
        node.pre, node.nex = l, r
        l.nex = r.pre = node
        self.cache[node.key] = node

    def pop(self, key: int) -> Node:
        node = self.cache.pop(key)
        l, r = node.pre, node.nex
        l.nex, r.pre = r, l
        return node

    def get(self, key: int) -> int:
        if node := self.cache.get(key):
            self.append(self.pop(key))
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if node := self.cache.get(key):
            node.value = value
            self.append(self.pop(key))
            return

        if len(self.cache) == self.cap:
            lru = self.left.nex
            self.pop(lru.key)
        self.append(Node(key, value))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
