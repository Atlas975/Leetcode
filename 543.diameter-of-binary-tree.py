#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from collections import defaultdict, deque


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # s, postord = deque([root]), defaultdict(int, {None: 0})
        # while s:
        #     node = s[-1]
        #     if node.left not in postord:
        #         s.append(node.left)
        #     elif node.right not in postord:
        #         s.append(node.right)
        #     else:
        #         node = s.pop()
        #         l_h, r_h = postord[node.left], postord[node.right]
        #         postord[node] = 1 + max(l_h, r_h)
        #         dpth = max(dpth, l_h + r_h)

        mxdpth = 0

        def dfs(node):
            nonlocal mxdpth
            if node is None:
                return 0
            l_h = dfs(node.left)
            r_h = dfs(node.right)
            mxdpth = max(mxdpth, l_h + r_h)
            return 1 + max(l_h, r_h)

        dfs(root)

        return mxdpth


# @lc code=end
