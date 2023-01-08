#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
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
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        unival = root.val

        def unirecur(root):
            if not root:
                return True
            if root.val != unival:
                return False
            return unirecur(root.left) and unirecur(root.right)

        return unirecur(root)

        # s = deque([root.left, root.right])

        # while s:
        #     if node := s.pop():
        #         if node.val != unival:
        #             return False
        #         s.append(node.left)
        #         s.append(node.right)
        # return True


# @lc code=end
