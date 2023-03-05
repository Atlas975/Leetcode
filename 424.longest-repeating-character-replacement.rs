/*
 * @lc app=leetcode id=424 lang=rust
 *
 * [424] Longest Repeating Character Replacement
 */

// @lc code=start
impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let mut freqs = [0; 128];
        let (mut res, mut l, mut mxfrq, k) = (0, 0, 0, k as usize);
        let s = s.as_bytes();

        for (r, &c) in s.into_iter().enumerate() {
            freqs[c as usize] += 1;
            mxfrq = mxfrq.max(freqs[c as usize]);
            if r - l + 1 - mxfrq > k {
                freqs[s[l] as usize] -= 1;
                l += 1;
            } else{
                res = res.max(r - l + 1);
            }
        }
        res as i32
    }
}
// @lc code=end

