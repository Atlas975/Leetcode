#
# @lc app=leetcode id=1410 lang=python3
#
# [1410] HTML Entity Parser
#

# @lc code=start
class Solution:
    def entityParser(self, text: str) -> str:
        html_map = {
            "&quot;": '"',
            "&apos;": "'",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/",
            "&amp;": "&",
        }
        for k, v in html_map.items():
            text = text.replace(k, v)
        return text


# @lc code=end
