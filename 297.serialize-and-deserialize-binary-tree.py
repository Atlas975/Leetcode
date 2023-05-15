#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        res = []

        def postord(node):
            if not node:
                res.append("null")
                return
            res.append(str(node.val))
            postord(node.left)
            postord(node.right)

        postord(root)
        return ",".join(res)

    def deserialize(self, data):
        def postord():
            val = next(data)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = postord()
            node.right = postord()
            return node

        data = iter(data.split(","))
        return postord()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
