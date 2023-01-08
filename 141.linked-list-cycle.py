#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slw, fst = head, head.next
        while slw != fst and (fst and fst.next):
            slw, fst = slw.next, fst.next.next

        return slw == fst


# @lc code=end
