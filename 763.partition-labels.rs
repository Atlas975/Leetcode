/*
 * @lc app=leetcode id=763 lang=rust
 *
 * [763] Partition Labels
 */

// @lc code=start
impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        let letters = s.chars().enumerate().fold([0; 26], |mut acc, (i, c)| {
            acc[c as usize - 97] = i;
            acc
        });

        let (mut l, mut r) = (0, 0);
        s.chars().enumerate().fold(vec![], |mut acc, (i, c)| {
            r = r.max(letters[c as usize - 97]);
            if i == r {
                acc.push((r - l + 1) as i32);
                l = r + 1;
            }
            acc
        })
    }
}
// @lc code=end

