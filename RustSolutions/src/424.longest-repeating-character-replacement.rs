/*
 * @lc app=leetcode id=424 lang=rust
 *
 * [424] Longest Repeating Character Replacement
 */

// @lc code=start
impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let mut freq = [0; 128];
        let (mut maxf, mut l, k) = (0, 0, k as usize);
        let s = s.as_bytes();

        s.iter().enumerate().fold(0, |acc, (r, &c)| {
            let idx = c as usize;
            freq[idx] += 1;
            maxf = maxf.max(freq[idx]);

            if r - l + 1 - maxf > k {
                freq[s[l] as usize] -= 1;
                l += 1;
                return acc;
            }
            acc.max(r - l + 1)
        }) as i32
    }
}
// @lc code=end
