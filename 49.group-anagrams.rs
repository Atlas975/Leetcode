/*
 * @lc app=leetcode id=49 lang=rust
 *
 * [49] Group Anagrams
 */

// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut res: HashMap<[u32; 26], Vec<String>> = HashMap::new();

        for s in strs {
            let mut key = [0; 26];
            for b in s.bytes() {
                key[(b - b'a') as usize] += 1;
            }
            res.entry(key).or_default().push(s);
        }
        res.into_iter().map(|(_, v)| v).collect()
    }
}
// @lc code=end

