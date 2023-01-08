#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        last, n = head, 1
        while last.next:
            last = last.next
            n += 1

        if k % n == 0:
            return head

        mid = head
        for _ in range(1, n - (k % n)):
            mid = mid.next

        res = mid.next
        last.next = head
        mid.next = None
        return res


# @lc code=end
