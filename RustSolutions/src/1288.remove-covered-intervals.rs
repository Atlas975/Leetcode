/*
 * @lc app=leetcode id=1288 lang=rust
 *
 * [1288] Remove Covered Intervals
 */

// @lc code=start
impl Solution {
    pub fn remove_covered_intervals(mut intervals: Vec<Vec<i32>>) -> i32 {
        intervals.sort_unstable_by(|a, b| {
            if a[0] == b[0] {
                b[1].cmp(&a[1])
            } else {
                a[0].cmp(&b[0])
            }
        });

        for

    }
}
// @lc code=end

