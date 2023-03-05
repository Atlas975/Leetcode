/*
 * @lc app=leetcode id=125 lang=rust
 *
 * [125] Valid Palindrome
 */

// @lc code=start
impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let (mut l, mut r) = (0, s.len() - 1);
        let s = s.as_bytes();

        while l < r {
            while !s[l].is_ascii_alphanumeric() && l < r {
                l += 1;
            }
            while !s[r].is_ascii_alphanumeric() && l < r {
                r -= 1;
            }
            if s[l].to_ascii_lowercase() != s[r].to_ascii_lowercase() {
                return false;
            }
            l += 1;
            r = r.saturating_sub(1);
        }
        true
    }
}
// @lc code=end
