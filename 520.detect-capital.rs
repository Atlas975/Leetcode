/*
 * @lc app=leetcode id=520 lang=rust
 *
 * [520] Detect Capital
 */

// @lc code=start
impl Solution {
    pub fn detect_capital_use(word: String) -> bool {
        let (mut upper, mut lower, n) = (0, 0, word.len());
        let fstup = word.chars().nth(0).unwrap().is_uppercase();

        for c in word.chars() {
            if c.is_uppercase() {
                upper += 1;
            } else {
                lower += 1;
            }
        }

        upper == n || lower == n || (fstup && lower == n - 1)
    }
}
// @lc code=end

