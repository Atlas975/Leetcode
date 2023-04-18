#
# @lc app=leetcode id=1115 lang=python3
#
# [1115] Print FooBar Alternately
#


# @lc code=start
from threading import Lock


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock, self.bar_lock = Lock(), Lock()
        self.bar_lock.acquire()


    def foo(self, printFoo: "Callable[[], None]") -> None:
        for _ in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar: "Callable[[], None]") -> None:
        for _ in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()

# @lc code=end
