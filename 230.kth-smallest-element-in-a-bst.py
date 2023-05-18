#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
import heapq


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # ITERATIVE
        s = deque([root])
        cur = root
        while s or cur:
            while cur:
                s.append(cur)
                cur = cur.left
            cur = s.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
        return -1
        
        # RECURSIVE
        self.k = k
        self.res = -1 

        def inorder(node) -> None:
            if node is None:
                return
            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            inorder(node.right)
        inorder(root)
        return self.res

# @lc code=end
