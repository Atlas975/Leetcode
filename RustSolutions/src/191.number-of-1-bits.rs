/*
 * @lc app=leetcode id=191 lang=rust
 *
 * [191] Number of 1 Bits
 */

// @lc code=start
impl Solution {
    pub fn hammingWeight(n: u32) -> i32 {
        if n == 0 {
            return 0;
        }
        1 + Self::hammingWeight(n & (n - 1))
    }
}
// @lc code=end
