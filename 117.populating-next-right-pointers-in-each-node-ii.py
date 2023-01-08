#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque


class Solution:
    def connect(self, root: "Node") -> "Node":
        # if root is None:
        #     return root
        # q = deque([root])
        # while q:
        #     for _ in range(len(q)-1):
        #         node = q.popleft()
        #         node.next = q[0]
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)

        #     node = q.popleft()
        #     node.next = None
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)

        def recur(node):


        return root


# @lc code=end
