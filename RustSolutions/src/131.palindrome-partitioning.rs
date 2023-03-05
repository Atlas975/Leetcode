/*
 * @lc app=leetcode id=131 lang=rust
 *
 * [131] Palindrome Partitioning
 */

// @lc code=start
impl Solution {
    pub fn partition(s: String) -> Vec<Vec<String>> {
        let valid_pali = |sbytes: &[u8]| -> bool {
            sbytes
                .iter()
                .take(sbytes.len() / 2)
                .enumerate()
                .all(|(i, &c)| c == sbytes[sbytes.len() - i - 1])
        };
    }
}
// @lc code=end
