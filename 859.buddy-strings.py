#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal and len(set(s)) < len(s):
            return True

        dif = []
        for a, b in zip(s, goal):
            if a != b:
                if len(dif) == 2:
                    return False
                dif.append((a, b))
        return len(dif) == 2 and dif[0] == dif[1][::-1]


# @lc code=end
