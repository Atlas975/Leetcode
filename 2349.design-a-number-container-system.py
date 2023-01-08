#
# @lc app=leetcode id=2349 lang=python3
#
# [2349] Design a Number Container System
#

# @lc code=start
from collections import defaultdict
import heapq


class NumberContainers:
    def __init__(self):
        self.i_n = defaultdict(int)
        self.n_i, self.n_iheap = defaultdict(set), defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if oldnum := self.i_n[index]:
            self.n_i[oldnum].remove(index)
            idxheap = self.n_iheap[oldnum]
            while idxheap and (idxheap[0] not in self.n_i[oldnum]):
                heapq.heappop(idxheap)

        self.i_n[index] = number
        self.n_i[number].add(index)
        heapq.heappush(self.n_iheap[number], index)

    def find(self, number: int) -> int:
        return self.n_iheap[number][0] if self.n_iheap[number] else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
# @lc code=end
