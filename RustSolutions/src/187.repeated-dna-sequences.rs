/*
 * @lc app=leetcode id=187 lang=rust
 *
 * [187] Repeated DNA Sequences
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn find_repeated_dna_sequences(s: String) -> Vec<String> {
        if s.len() < 10 {
            return Vec::new();
        }
        let mut res : Vec<String> = Vec::new();
        let mut seen = HashMap::new();
        seen.insert(&s[0..10], 1);

        for i in 1..(s.len() - 9) {
            let sub = &s[i..(i + 10)];
            let cnt = seen.entry(sub).or_insert(0);
            if *cnt == 1 {
                res.push(sub.to_owned());
            }
            *cnt += 1;
        }
        res
    }
}
// @lc code=end

