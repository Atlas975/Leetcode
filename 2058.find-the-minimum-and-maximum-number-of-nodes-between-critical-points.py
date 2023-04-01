#
# @lc app=leetcode id=2058 lang=python3
#
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return (-1, -1)
        prev = head.val
        head = head.next
        mindist = float("inf")
        maxdist = -1 
        res = []
        idx = 2
        while head.next:
            curr = head.val
            post = head.next.val
            if (prev > curr and post > curr) or (prev < curr and post < curr):
                if res:
                    mindist = min(mindist, idx - res[-1])
                    maxdist = idx - res[0]
                res.append(idx)
            prev = curr
            head = head.next
            idx += 1
        return (-1, -1) if len(res) <= 1 else (mindist, maxdist)


# @lc code=ed
