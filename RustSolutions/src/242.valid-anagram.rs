/*
 * @lc app=leetcode id=242 lang=rust
 *
 * [242] Valid Anagram
 */

// @lc code=start
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let (mut scnt, mut tcnt) = ([0; 26], [0; 26]);
        
    }
}
// @lc code=end

