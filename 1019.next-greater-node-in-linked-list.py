#
# @lc app=leetcode id=1019 lang=python3
#
# [1019] Next Greater Node In Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res, stack = [0], deque([(0, head.val)])

        while head := head.next:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val

            stack.append((len(res), head.val))
            res.append(0)

        return res


# @lc code=end
