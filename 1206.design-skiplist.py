#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#

# @lc code=start

from dataclasses import dataclass


@dataclass
class Node:
    val: int
    pos: "Node"
    pre: "Node"

class Skiplist:

    def __init__(self):


    def search(self, target: int) -> bool:


    def add(self, num: int) -> None:


    def erase(self, num: int) -> bool:



# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end

