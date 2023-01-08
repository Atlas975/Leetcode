#
# @lc app=leetcode id=2424 lang=python3
#
# [2424] Longest Uploaded Prefix
#

# @lc code=start


class LUPrefix:
    def __init__(self, n: int):
        self.res = 0
        self.server = set()

    def upload(self, video: int) -> None:
        self.server.add(video)
        while self.res + 1 in self.server:
            self.res += 1

    def longest(self) -> int:
        return self.res


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
# @lc code=end
