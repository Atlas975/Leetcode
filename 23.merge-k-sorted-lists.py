#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        minheap = []
        for head in lists:
            while head:
                heapq.heappush(minheap, (head.val, head))
                head = head.next

        dmy = ListNode()
        while minheap:
            _, node = heapq.heappop(minheap)
            dmy.next = node
            dmy = dmy.next

        return dmy.next


# @lc code=end
