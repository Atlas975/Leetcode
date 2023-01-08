#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import List, Optional


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        res = []
        s, visited = deque([root]), {None}
        while s:
            node = s[-1]
            if node.left not in visited:
                s.append(node.left)
            elif node.right not in visited:
                s.append(node.right)
            else:
                node = s.pop()
                visited.add(node)
                res.append(node.val)
        return res


# @lc code=end
