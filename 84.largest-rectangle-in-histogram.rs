/*
 * @lc app=leetcode id=84 lang=rust
 *
 * [84] Largest Rectangle in Histogram
 */

// @lc code=start
use std::collections::VecDeque;

impl Solution {
    pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
        let (mut mxar, mut s) = (0, VecDeque::new());
        for (r, &h) in heights.iter().enumerate() {
            let mut l = r;

            while s.back().map_or(false, |&(_, h0)| h0 > h) {
                let (l0, h0) = s.pop_back().unwrap();
                mxar = mxar.max(h0 * (r - l0) as i32);
                l = l0;
            }
            s.push_back((l, h));
        }

        let n = heights.len();
        mxar.max(
            s.iter()
                .fold(0, |mx, &(l0, h0)| mx.max(h0 * (n - l0) as i32)),
        )
    }
}
// @lc code=end
