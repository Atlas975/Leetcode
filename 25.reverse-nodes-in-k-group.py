#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        tailpre = dmy = ListNode(next=head)
        def getKth(cur, k) -> ListNode:
            for _ in range(k):
                if not cur:
                    return None
                cur = cur.next
            return cur

        while kth := getKth(tailpre, k):
            cur, prev = tailpre.next, kth.next # head of group, head of next group
            for _ in range(k): # k nodes in group to reverse
                cur.next, cur, prev = prev, cur.next, cur
            tailpre.next, tailpre = kth, tailpre.next # connect prev group to this groups old tail 
        return dmy.next


# @lc code=end
