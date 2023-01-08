#
# @lc app=leetcode id=468 lang=python3
#
# [468] Validate IP Address
#

# @lc code=start
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ipv4 = r"^$"
        ipv6
        if queryIP.find(".") > 0:
            xi = queryIP.split(".")
            if len(xi) != 4:
                return "Neither"
            for substr in xi:
                try:
                    if (len(substr) > 1 and substr[0] == "0") or (
                        int(substr) not in range(256)
                    ):
                        return "Neither"
                except ValueError:
                    return "Neither"
            return "IPv4"

        if queryIP.find(":") > 0:
            xi = queryIP.split(":")
            if len(xi) != 8 or any(len(x) not in range(1, 5) for x in xi):
                return "Neither"
            try:
                [int(x, 16) for x in xi]
            except ValueError:
                return "Neither"
            return "IPv6"

        return "Neither"

        # print(xi)


# @lc code=end
