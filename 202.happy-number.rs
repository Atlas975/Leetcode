/*
 * @lc app=leetcode id=202 lang=rust
 *
 * [202] Happy Number
 */

// @lc code=start
use std::collections::HashSet;
impl Solution {
    pub fn is_happy(mut n: i32) -> bool {
        let digsum = move |n: i32| -> i32 {
            let mut s = 0;
            while n > 0 {
                s += (n % 10).pow(2);
                n /= 10;
            }
            s
        };
        loop {
            let mut s = 0;
            while n > 0 {
                s += (n % 10).pow(2);
                n /= 10;
            }
            match s {
                1 | 4 => break s == 1, // 4 results in a loop
                _ => n = s,
            }
        }
    }
}
// @lc code=end
