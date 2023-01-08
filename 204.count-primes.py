#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        seq = [0, 0] + [1] * (n - 2)
        root = int(n**0.5) + 1
        for i in range(2, root):
            if seq[i]:
                for j in range(i * i, n, i):
                    seq[j] = 0
        return sum(seq)


# @lc code=end
