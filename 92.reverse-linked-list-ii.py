#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        tmp = ListNode(0, head)
        pre = tmp

        for _ in range(left - 1):
            pre = pre.next

        lbound = pre.next
        start = lbound.next

        for _ in range(right - left):
            lbound.next = start.next
            start.next = pre.next
            pre.next = start
            start = lbound.next

        return tmp.next


# @lc code=end
