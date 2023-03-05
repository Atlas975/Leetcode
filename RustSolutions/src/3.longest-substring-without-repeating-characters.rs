/*
 * @lc app=leetcode id=3 lang=rust
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut seen = [usize::MAX; 128];
        let (mut res, mut l) = (0, 0);

        for (r, c) in s.bytes().map(|c| c as usize).enumerate() {
            if seen[c] != usize::MAX {
                l = l.max(seen[c] + 1);
            }
            seen[c] = r;
            res = res.max(r - l + 1);
        }
        res as i32
    }
}
// @lc code=end

