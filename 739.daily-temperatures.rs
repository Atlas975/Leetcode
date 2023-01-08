/*
 * @lc app=leetcode id=739 lang=rust
 *
 * [739] Daily Temperatures
 */

// @lc code=start
use std::collections::VecDeque;

impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let mut res = vec![0; temperatures.len()];
        let mut s = VecDeque::new();

        for (r, &t) in temperatures.iter().enumerate() {
            while let Some(&last) = s.back() {
                if temperatures[last] < t {
                    let l = s.pop_back().unwrap();
                    res[l] = r as i32 - l as i32;
                } else {
                    break;
                }
            }
            s.push_back(r);
        }
        res
    }
}
// @lc code=end
