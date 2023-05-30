from typing import (
    List,
)


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
        staptrs = sorted(m[0] for m in intervals)
        endptrs = sorted(m[1] for m in intervals)
        sptr, eptr = 1, 0
        rooms = mxrooms = 1

        while sptr < len(staptrs):
            if staptrs[sptr] >= endptrs[eptr]: # no overlap
                eptr += 1
                rooms -= 1
            else:
                sptr += 1
                rooms += 1
                mxrooms = max(mxrooms, rooms)
        return mxrooms