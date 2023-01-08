#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start

from dataclasses import dataclass


@dataclass
class 
class MyLinkedList:

    def __init__(self,val=0):
        self.next=None
        self.val=val

    def get(self, index: int) -> int:
        pass

    def addAtHead(self, val: int) -> None:
        if self.next is None:
            self.next=MyLinkedList(val)
        node=self.next
        self.next=




    def addAtTail(self, val: int) -> None:


    def addAtIndex(self, index: int, val: int) -> None:


    def deleteAtIndex(self, index: int) -> None:



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

