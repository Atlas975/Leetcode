/*
 * @lc app=leetcode id=763 lang=rust
 *
 * [763] Partition Labels
 */

// @lc code=start
impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        let mut res = vec![];
        let lstidx = s.bytes().enumerate().fold([0; 26], |mut lstidx, (i, c)| {
            lstidx[(c - b'a') as usize] = i;
            lstidx
        });

        let (mut l, mut r) = (0, 0);
        for (i, c) in s.bytes().enumerate() {
            r = r.max(lstidx[(c - b'a') as usize]);
            if i == r {
                res.push((r - l + 1) as i32);
                l = r + 1;
            }
        }
        res
    }
}
// @lc code=end

