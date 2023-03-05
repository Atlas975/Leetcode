/*
 * @lc app=leetcode id=155 lang=rust
 *
 * [155] Min Stack
 */

// @lc code=start
use std::collections::VecDeque;

struct MinStack {
    s: VecDeque<(i32, i32)>,
}

impl MinStack {
    fn new() -> Self {
        Self { s: VecDeque::new() }
    }

    fn push(&mut self, val: i32) {
        let smin = if self.s.is_empty() {val} else {self.get_min()};
        self.s.push_back((val, val.min(smin)));
    }

    fn pop(&mut self) {
        self.s.pop_back();
    }

    fn top(&self) -> i32 {
        self.s.back().unwrap().0
    }

    fn get_min(&self) -> i32 {
        self.s.back().unwrap().1
    }
}
/**
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack::new();
 * obj.push(val);
 * obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.get_min();
 */
// @lc code=end

