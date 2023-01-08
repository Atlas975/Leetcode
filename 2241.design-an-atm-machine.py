#
# @lc app=leetcode id=2241 lang=python3
#
# [2241] Design an ATM Machine
#

# @lc code=start


class ATM:
    def __init__(self):
        self.notevalue = [20, 50, 100, 200, 500]
        self.notecount = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, note in enumerate(banknotesCount):
            self.notecount[i] += note

    def withdraw(self, amount: int) -> List[int]:
        give = [0] * 5

        for i in range(4, -1, -1):
            give[i] = min(self.notecount[i], amount // self.notevalue[i])
            amount -= give[i] * self.notevalue[i]
            if amount == 0:
                break

        if amount > 0:
            return [-1]
        for i, g in enumerate(give):
            self.notecount[i] -= g
        return give


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
# @lc code=end
