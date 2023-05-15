#
# @lc app=leetcode id=2512 lang=python3
#
# [2512] Reward Top K Students
#

# @lc code=start
from collections import defaultdict
import heapq


class Solution:
    def topStudents(
        self, pos: List[str], neg: List[str], report: List[str], student_id: List[int], k: int
    ) -> List[int]:

        pos, neg = set(pos), set(neg)

        res = []
        for id, report in zip(student_id, report):
            score = 0
            for word in report.split():
                if word in pos:
                    score += 3
                elif word in neg:
                    score -= 1
            res.append((-score, id))
        return (each[1] for each in heapq.nsmallest(k, res))


# @lc code=end
