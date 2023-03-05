/*
 * @lc app=leetcode id=268 lang=rust
 *
 * [268] Missing Number
 */

// @lc code=start
impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        nums.into_iter()
            .enumerate()
            .fold(n, |acc, (i, x)| acc ^ (i as i32) ^ x)
    }
}
// @lc code=end
