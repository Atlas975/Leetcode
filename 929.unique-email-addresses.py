#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mailset = set()
        for email in emails:
            loc, dom = email.split("@")
            loc = loc.split("+")[0].replace(".", "")
            mailset.add(f"{loc}@{dom}")
        return len(mailset)


# @lc code=end
