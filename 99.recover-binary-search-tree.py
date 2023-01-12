#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        n1, n2 = None, None
        pre = TreeNode(float("-inf"))
        s = deque()

        while root or s:
            while root:
                s.append(root)
                root = root.left
            root = s.pop()

            if pre.val > root.val:
                if n1:
                    n1.val, root.val = root.val, n1.val
                    return
                n1 = pre
                n2 = root

            pre = root
            root = root.right

        n1.val, n2.val = n2.val, n1.val


# @lc code=end
