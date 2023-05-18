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
        while fst and fst.next:  # if odd, slw stops at mid else n/2
            slw = slw.next
            fst = fst.next.next

        cur = slw.next
        fst = slw.next = None
        while cur:  # reverse second half
            cur.next, fst, cur = fst, cur, cur.next

        while fst:  # merge
            l1_nex, l2_nex = head.next, fst.next
            head.next, fst.next = fst, l1_nex
            head, fst = l1_nex, l2_nex


# @lc code=end
