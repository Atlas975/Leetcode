/*
 * @lc app=leetcode id=53 lang=rust
 *
 * [53] Maximum Subarray
 */

// @lc code=start
impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        nums.iter().fold((0, i32::min_value()), |(sum, mxsub), &num| {
            let sum = if sum > 0 { sum + num } else { num };
            (sum, mxsub.max(sum))
        }).1
    }
}
// @lc code=end

