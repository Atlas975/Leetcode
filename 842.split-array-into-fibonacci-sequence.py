#
# @lc app=leetcode id=842 lang=python3
#
# [842] Split Array into Fibonacci Sequence
#

# @lc code=start
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        grps = []
        U32_MAX = 2**31 - 1

        def dfs(seq):
            if not seq:
                return len(grps) >= 3

            if seq[0] == "0":
                if len(grps) < 2 or grps[-1] + grps[-2] == 0:
                    grps.append(0)
                    if dfs(seq[1:]):
                        return True
                    grps.pop()
                return False

            for i in range(1, len(seq) + 1):
                cur = int(seq[:i])
                if cur > U32_MAX:
                    break

                if len(grps) < 2 or cur == grps[-1] + grps[-2]:
                    grps.append(cur)
                    if dfs(seq[i:]):
                        return True
                    grps.pop()
            return False

        dfs(num)
        return grps


# @lc code=end
