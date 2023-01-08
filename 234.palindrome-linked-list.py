#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = head
        endmap = {}

        n = 0
        while tmp:
            endmap[n] = tmp.val
            tmp = tmp.next
            n += 1

        return all(endmap[i] == endmap[n - i - 1] for i in range(n // 2))


# @lc code=end
