#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        doublemp, halfmp = set(), set()
        for num in arr:
            if num in doublemp or num in halfmp:
                return True
            doublemp.add(num * 2)
            halfmp.add(num / 2)
        return False
        # return any(n1 == 2 * n2 for n1, n2 in permutations(arr, 2))


# @lc code=end
