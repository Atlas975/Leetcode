#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Merge-sort solution
        def merge(l1, l2):
            dmy = cur = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            elif l2:
                cur.next = l2
            return dmy.next

        while (n := len(lists)) > 1:
            rem = n % 2
            for i in range(0, n - rem, 2):
                lists[i // 2] = merge(lists[i], lists[i + 1])
            if rem:
                lists[n // 2] = lists[-1]
            lists = lists[: n // 2 + rem]
        return lists[0] if lists else None

        # Min-heap solution
        pq = [(ll.val, i, ll) for i, ll in enumerate(filter(None, lists))]
        heapq.heapify(pq)

        dmy = cur = ListNode()
        while pq:
            _, i, ll = heapq.heappop(pq)
            cur.next, cur = ll, ll
            if post := ll.next:
                heapq.heappush(pq, (post.val, i, post))
        return dmy.next


# @lc code=end
