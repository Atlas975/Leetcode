#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = []
        q = deque([root])
        reverse = False

        while q:
            level = deque()

            for _ in range(len(q)):
                node = q.popleft()
                if reverse:
                    level.appendleft(node.val)
                else:
                    level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            reverse = not reverse
            res.append(level)

        return res


# @lc code=end
