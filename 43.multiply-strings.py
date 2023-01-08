#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        digits = [0] * (n1 + n2)

        for i in reversed(range(n1)):
            if num1[i] == "0":
                continue
            for j in reversed(range(n2)):
                digits[i + j + 1] += int(num1[i]) * int(num2[j])
                digits[i + j] += digits[i + j + 1] // 10
                digits[i + j + 1] %= 10
        return "".join(map(str, digits)).lstrip("0") or "0"


# @lc code=end
