#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        carry = 0
        head = dmy = ListNode()

        while l1 and l2:
            carry += l1.val + l2.val
            dmy.next = ListNode(carry % 10)
            l1, l2, dmy = l1.next, l2.next, dmy.next
            carry //= 10

        while l1:
            carry += l1.val
            dmy.next = ListNode(carry % 10)
            l1, dmy = l1.next, dmy.next
            carry //= 10
        while l2:
            carry += l2.val
            dmy.next = ListNode(carry % 10)
            l2, dmy = l2.next, dmy.next
            carry //= 10
        if carry:
            dmy.next = ListNode(carry)

        return head.next


# @lc code=end
