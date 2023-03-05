#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start


from itertools import dropwhile, product


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        digits = [0] * (n1 + n2)

        for i, j in product(filter(lambda i: num1[i] != "0", range(n1 - 1, -1, -1)), range(n2 - 1, -1, -1)):
            digits[i + j + 1] += (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
            digits[i + j] += digits[i + j + 1] // 10
            digits[i + j + 1] %= 10
        return "".join(map(str, dropwhile(lambda d: d == 0, digits))) or "0"


# @lc code=end
