#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slw, fst = head, head.next
        while fst and fst.next:  # find middle
            slw = slw.next
            fst = fst.next.next

        curr = slw.next
        fsthead = slw.next = None
        while curr:  # reverse second half
            nex = curr.next
            curr.next = fsthead
            fsthead = curr
            curr = nex

        while fsthead:  # merge
            nex1, nex2 = head.next, fsthead.next
            head.next, fsthead.next = fsthead, nex1
            head, fsthead = nex1, nex2


# @lc code=end
