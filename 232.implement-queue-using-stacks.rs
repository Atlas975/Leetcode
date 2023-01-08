/*
 * @lc app=leetcode id=232 lang=rust
 *
 * [232] Implement Queue using Stacks
 */

// @lc code=start
use std::collections::VecDeque;

struct MyQueue {
    s1: VecDeque<i32>,
    s2: VecDeque<i32>,
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyQueue {

    fn new() -> Self {
        MyQueue { s1: VecDeque::new(), s2: VecDeque::new() }
    }

    fn push(&mut self, x: i32) {
        self.s1.push_back(x);
    }

    fn stk_to_que(&mut self) {
        if self.s2.is_empty() {
            while let Some(x) = self.s1.pop_back() {
                self.s2.push_back(x);
            }
        }
    }

    fn pop(&mut self) -> i32 {
        self.stk_to_que();
        self.s2.pop_back().unwrap()
    }

    fn peek(&mut self) -> i32 {
        self.stk_to_que();
        *self.s2.back().unwrap()
    }

    fn empty(&self) -> bool {
        self.s1.is_empty() && self.s2.is_empty()
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj = MyQueue::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.peek();
 * let ret_4: bool = obj.empty();
 */
// @lc code=end

