#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# from collections import deque
from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # return maxdepth
        # if root is None:
        #     return 0
        # mxdpth = 0
        # s = deque([(root, 1)])
        # while s:
        #     node, depth = s.pop()
        #     mxdpth = max(mxdpth, depth)
        #     if node.left:
        #         s.append((node.left, depth + 1))
        #     if node.right:
        #         s.append((node.right, depth + 1))
        # return mxdpth


# @lc code=end
