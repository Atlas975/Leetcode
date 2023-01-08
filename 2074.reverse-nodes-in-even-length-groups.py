#
# @lc app=leetcode id=2074 lang=python3
#
# [2074] Reverse Nodes in Even Length Groups
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, grpsze = head, 2
        while prev.next:
            tmp, i = prev, 0
            while tmp.next and i < grpsze:
                tmp, i = tmp.next, i + 1
            if i & 1:
                prev = tmp
            else:
                grphd = grptl = prev.next
                rev = None
                for _ in range(i):
                    rev, grphd.next, grphd = grphd, rev, grphd.next
                grptl.next, prev.next, prev = grphd, rev, prev.next
            grpsze += 1
        return head


# @lc code=end
