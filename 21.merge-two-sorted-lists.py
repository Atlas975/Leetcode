#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 or not list2:
            return list1 or list2
        dmy = curr = ListNode()

        while list1 or list2:
            l1val = list1.val if list1 else float("inf")
            l2val = list2.val if list2 else float("inf")

            if l1val < l2val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        return dmy.next


# @lc code=end
