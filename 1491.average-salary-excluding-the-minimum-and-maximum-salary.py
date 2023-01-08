#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start
class Solution:
    def average(self, salary: List[int]) -> float:
        minsal, maxsal = float("inf"), float("-inf")
        sumsal = 0
        for sal in salary:
            minsal = min(minsal, sal)
            maxsal = max(maxsal, sal)
            sumsal += sal
        return (sumsal - minsal - maxsal) / (len(salary) - 2)


# @lc code=end
