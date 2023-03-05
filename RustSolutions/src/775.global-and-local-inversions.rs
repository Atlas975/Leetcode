/*
 * @lc app=leetcode id=775 lang=rust
 *
 * [775] Global and Local Inversions
 */

// @lc code=start
impl Solution {
    pub fn is_ideal_permutation(nums: Vec<i32>) -> bool {
        nums.into_iter()
            .enumerate()
            .all(|(i, v)| matches!(v - i as i32, 0 | 1 | -1))
    }
}
// @lc code=end
