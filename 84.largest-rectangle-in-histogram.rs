/*
 * @lc app=leetcode id=84 lang=rust
 *
 * [84] Largest Rectangle in Histogram
 */

// @lc code=start

use std::collections::VecDeque;

impl Solution {
    pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
        let (mut s, mut mxrea) = (VecDeque::new(), 0);

        for (r, h) in heights.iter().enumerate() {
            let mut strt = r;
            while let Some(&(l, lsth)) = s.back() {
                if lsth <= h {
                    break;
                }
                s.pop_back();
                mxrea = mxrea.max(lsth * (r - l) as i32);
                strt = l;
            }
            s.push_back((strt, h));
        }

        let n = heights.len();
        for (l, h) in s {
            mxrea = mxrea.max(h * (n - l) as i32);
        }

        mxrea
    }
}
// @lc code=end
