#
# @lc app=leetcode id=1226 lang=python3
#
# [1226] The Dining Philosophers
#

# @lc code=start
from threading import Lock


class DiningPhilosophers:
    def __init__(self):
        self.locks = [Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork: "Callable[[], None]",
        pickRightFork: "Callable[[], None]",
        eat: "Callable[[], None]",
        putLeftFork: "Callable[[], None]",
        putRightFork: "Callable[[], None]",
    ) -> None:



        f1, f2 = (1, 0) if philosopher == 0 else (philosopher, (philosopher + 1) % 5)

        with (self.locks[f1], self.locks[f2]):
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()



# @lc code=end
