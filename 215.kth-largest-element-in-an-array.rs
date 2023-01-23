/*
 * @lc app=leetcode id=215 lang=rust
 *
 * [215] Kth Largest Element in an Array
 */

// @lc code=start
impl Solution {
    pub fn find_kth_largest(mut nums: Vec<i32>, k: i32) -> i32 {
        *nums
            .select_nth_unstable_by((k - 1) as usize, |a, b| b.cmp(a))
            .1
    }
}
// @lc code=end
