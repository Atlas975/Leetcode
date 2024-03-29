/*
 * @lc app=leetcode id=150 lang=rust
 *
 * [150] Evaluate Reverse Polish Notation
 */

// @lc code=start
use std::collections::VecDeque;

impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut s = VecDeque::new();
        for t in tokens {
            if let Ok(t) = t.parse::<i32>() {
                s.push_back(t);
            } else {
                let (n2, n1) = (s.pop_back().unwrap(), s.pop_back().unwrap());
                s.push_back(match t.as_str() {
                    "+" => n1 + n2,
                    "-" => n1 - n2,
                    "*" => n1 * n2,
                    "/" => n1 / n2,
                    _ => unreachable!(),
                });
            }
        }
        s.pop_back().unwrap()
    }
}
// @lc code=end 
