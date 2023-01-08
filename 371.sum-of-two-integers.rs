/*
 * @lc app=leetcode id=371 lang=rust
 *
 * [371] Sum of Two Integers
 */

// @lc code=start
impl Solution {
    pub fn get_sum(a: i32, b: i32) -> i32 {
        fn add(a: i32, b: i32) -> i32 {
            if b == 0 {
                return a;
            }
            add(a ^ b, (a & b) << 1)
        }
        return add(a, b);
    }
}
// @lc code=end

