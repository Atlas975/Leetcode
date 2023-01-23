/*
 * @lc app=leetcode id=20 lang=rust
 *
 * [20] Valid Parentheses
 */

// @lc code=start
use std::collections::VecDeque;
impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = VecDeque::new();
        for c in s.chars() {
            match c {
                '{' => stack.push_back('}'),
                '(' => stack.push_back(')'),
                '[' => stack.push_back(']'),
                '}' | ')' | ']' if Some(c) != stack.pop_back() => return false,
                _ => (),
            }
        }
        stack.is_empty()
    }
}
// @lc code=end

