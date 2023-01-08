#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dum = ListNode(next=head)
        l, r = dum, head

        for _ in range(n):
            r = r.next

        while r:
            l, r = l.next, r.next

        l.next = l.next.next
        return dum.next


# @lc code=end
