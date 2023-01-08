#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
class MyHashSet:
    def __init__(self):
        self.vals = [False] * 1_000_001

    def add(self, key: int) -> None:
        self.vals[key] = True

    def remove(self, key: int) -> None:
        self.vals[key] = False

    def contains(self, key: int) -> bool:
        return self.vals[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end
