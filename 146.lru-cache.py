#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start


class Node:
    def __init__(p, key=0, value=0, pre=None, nex=None):
        p.key = key
        p.value = value
        p.pre = pre
        p.nex = nex


class LRUCache:
    def __init__(p, cap: int):
        p.cap = cap
        p.cache = {}
        p.left, p.right = Node(), Node()
        p.left.nex, p.right.pre = p.right, p.left

    def append(p, node: Node) -> None:
        l, r = p.right.pre, p.right
        node.pre, node.nex = l, r
        l.nex = r.pre = node
        p.cache[node.key] = node

    def pop(p, key: int) -> Node:
        node = p.cache.pop(key)
        l, r = node.pre, node.nex
        l.nex, r.pre = r, l
        return node

    def get(p, key: int) -> int:
        if node := p.cache.get(key):
            p.append(p.pop(key))
            return node.value
        return -1

    def put(p, key: int, value: int) -> None:
        if node := p.cache.get(key):
            node.value = value
            p.append(p.pop(key))
            return

        if len(p.cache) == p.cap:
            lru = p.left.nex
            p.pop(lru.key)
        p.append(Node(key, value))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
