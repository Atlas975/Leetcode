/*
 * @lc app=leetcode id=853 lang=rust
 *
 * [853] Car Fleet
 */

// @lc code=start

use std::collections::VecDeque;

impl Solution {
    pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
        let mut pairs = position
            .into_iter()
            .zip(speed.into_iter())
            .collect::<Vec<_>>();
        pairs.sort_by(|(p1, _), (p2, _)| p2.cmp(p1));

        let (p1, s1) = pairs[0];
        let mut stack = VecDeque::new();
        stack.push_back((p1, (target - p1) as f64 / s1 as f64));

        for &(p, s) in &pairs[1..] {
            let t = (target - p) as f64 / s as f64;
            if t > stack.back().unwrap().1 {
                stack.push_back((p, t));
            }
        }
        stack.len() as i32
    }
}
// @lc code=end
