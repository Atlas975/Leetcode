#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letmp = [
            [],
            [],
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
            ["j", "k", "l"],
            ["m", "n", "o"],
            ["p", "q", "r", "s"],
            ["t", "u", "v"],
            ["w", "x", "y", "z"],
        ]

        def backtrack(i, s):
            if i >= len(digits):
                res.append(s)
                return
            for c in letmp[int(digits[i])]:
                backtrack(i + 1, s + c)
        res = []
        backtrack(0, "")
        return res

        # DYANMIC PROGRAMMING
        n = len(digits)
        dp = [[] for _ in range(n)]
        dp[-1] = letmp[int(digits[-1])]

        for i in reversed(range(n - 1)):
            for l in letmp[int(digits[i])]:
                dp[i].extend([l + sub for sub in dp[i + 1]])
        return dp[0]


# @lc code=end
