#
# @lc app=leetcode id=1462 lang=python3
#
# [1462] Course Schedule IV
#

# @lc code=start
class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        req = {preq[1]: preq[0] for preq in prerequisites}
        res = []
        for query in queries:
            if query[0] in req and req[query[0]] in numCourses:
                res.append(True)
            else:
                res.append(False)
        return res


# @lc code=end
