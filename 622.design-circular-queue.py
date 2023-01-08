#
# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#

# @lc code=start

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class Node:
    val: int
    nex: Optional["Node"] = None
    pre: Optional["Node"] = None


class MyCircularQueue:
    def __init__(self, k: int):
        self.space = k
        self.l = Node(0)
        self.r = Node(0, pre=self.l)
        self.l.nex = self.r

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        cur = Node(value, self.r, self.r.pre)
        self.r.pre.nex = cur
        self.r.pre = cur
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.l.nex = self.l.nex.nex
        self.l.nex.pre = self.l
        self.space += 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.l.nex.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.r.pre.val

    def isEmpty(self) -> bool:
        return self.l.nex == self.r

    def isFull(self) -> bool:
        return self.space == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end
