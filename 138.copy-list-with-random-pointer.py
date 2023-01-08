#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
# Definition for a Node.


# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None
        tmp, clonemp = head, {}
        getClone = lambda k: clonemp.setdefault(k, Node(k.val)) if k else None

        while tmp:
            clonemp[tmp] = getClone(tmp)
            clonemp[tmp].next = getClone(tmp.next)
            clonemp[tmp].random = getClone(tmp.random)
            tmp = tmp.next

        return clonemp[head]


# @lc code=end
