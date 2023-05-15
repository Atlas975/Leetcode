#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        idx = lambda c: ord(c) - ord("a")

        s1cnt, win = [0] * 26, [0] * 26
        for c1, c2 in zip(s1, s2):
            s1cnt[idx(c1)] += 1
            win[idx(c2)] += 1
        matches = sum(c1 == c2 for c1, c2 in zip(s1cnt, win))

        for i in range(n1, n2):
            if matches == 26:
                return True
            l, r = idx(s2[i - n1]), idx(s2[i])

            win[r] += 1
            if s1cnt[r] == win[r]:
                matches += 1
            elif s1cnt[r] + 1 == win[r]:
                matches -= 1

            win[l] -= 1
            if s1cnt[l] == win[l]:
                matches += 1
            elif s1cnt[l] - 1 == win[l]:
                matches -= 1

        return matches == 26


# @lc code=end
