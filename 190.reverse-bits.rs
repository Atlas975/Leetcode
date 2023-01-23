/*
 * @lc app=leetcode id=190 lang=rust
 *
 * [190] Reverse Bits
 */

// @lc code=start
impl Solution {
    pub fn reverse_bits(x: u32) -> u32 {
        let mut x = x;
        (0..32).fold(0, |mut acc, _| {
            acc <<= 1;
            acc |= x & 1;
            x >>= 1;
            acc
        })
    }
}
// @lc code=end
