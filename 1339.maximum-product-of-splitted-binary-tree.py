#
# @lc app=leetcode id=1339 lang=python3
#
# [1339] Maximum Product of Splitted Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []

        def total(root):
            if root is None:
                return 0
            sums.append(total(root.left) + total(root.right) + root.val)
            return sums[-1]

        rootsum = total(root)
        optimal = rootsum // 2
        closest = min(sums, key=lambda x: abs(x - optimal))
        return ((rootsum - closest) * closest) % (10**9 + 7)


# @lc code=end
