/*
 * @lc app=leetcode id=338 lang=rust
 *
 * [338] Counting Bits
 */

// @lc code=start
impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        if n == 0 {
            return vec![0];
        }
        let n = n as usize;
        let mut res = vec![0; n + 1];
        res[1] = 1;
        for i in 2..=n {
            res[i] = res[i >> 1] + (i & 1) as i32;
        }
        res
    }
}
// @lc code=end

