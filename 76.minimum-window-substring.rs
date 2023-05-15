/*
 * @lc app=leetcode id=76 lang=rust
 *
 * [76] Minimum Window Substring
 */

// @lc code=start
impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        let (sn, tn) = (s.len(), t.len());
        let (sbytes, tbytes) = (s.as_bytes(), t.as_bytes());
        if sn < tn {
            return "".to_owned();
        }
        let idx = |c: &u8| -> usize { (c - b'A') as usize };
        let mut need = [0; 58];
        let mut res = (0, usize::max_value());

        for c in tbytes.iter().map(|c| idx(c)) {
            need[c] += 1;
        }
        let (mut l, mut needcnt) = (0, tn);

        for (r, c) in sbytes.iter().map(|c| idx(c)).enumerate() {
            if need[c] > 0 {
                needcnt -= 1;
            }
            need[c] -= 1;
            if needcnt > 0 {
                continue;
            }
            while need[idx(&sbytes[l])] < 0 {
                need[idx(&sbytes[l])] += 1;
                l += 1;
            }
            if r - l < res.1 - res.0 {
                res = (l, r);
            }
            need[idx(&sbytes[l])] += 1;
            needcnt += 1;
            l += 1;
        }

        if res.1 == usize::max_value() {
            return "".to_owned();
        }
        s[res.0..=res.1].to_owned()
    }
}
// @lc code=end
