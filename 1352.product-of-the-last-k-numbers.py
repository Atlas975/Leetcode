#
# @lc app=leetcode id=1352 lang=python3
#
# [1352] Product of the Last K Numbers
#

# @lc code=start


class ProductOfNumbers:
    def __init__(self):
        self.stack = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.stack = [1]
        else:
            self.stack.append(num * self.stack[-1])

    def getProduct(self, k: int) -> int:
        return self.stack[-1] // self.stack[-k - 1] if k < len(self.stack) else 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
# @lc code=end
