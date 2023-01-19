/*
 * @lc app=leetcode id=1732 lang=rust
 *
 * [1732] Find the Highest Altitude
 */

// @lc code=start
impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        gain.into_iter()
            .fold((0, 0), |(tgain, mxalt), g| {
                (tgain + g, mxalt.max(tgain + g))
            })
            .1
    }
}
// @lc code=end
