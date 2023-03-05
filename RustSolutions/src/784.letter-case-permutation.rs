/*
 * @lc app=leetcode id=784 lang=rust
 *
 * [784] Letter Case Permutation
 */

// @lc code=start
use std::collections::VecDeque;
impl Solution {
    pub fn letter_case_permutation(s: String) -> Vec<String> {
        let (mut res, mut substr) = (vec![], VecDeque::new());

        fn dfs(substr: &mut VecDeque<char>, s: &str, res: &mut Vec<String>) {
            let sublen = substr.len();
            if sublen == s.len() {
                res.push(substr.iter().collect());
            } else if let Some(c) = s.chars().nth(sublen) {
                if c.is_ascii_alphabetic() {
                    substr.push_back(c.to_ascii_lowercase());
                    dfs(substr, s, res);
                    substr.pop_back();

                    substr.push_back(c.to_ascii_uppercase());
                    dfs(substr, s, res);
                    substr.pop_back();
                } else {
                    substr.push_back(c);
                    dfs(substr, s, res);
                    substr.pop_back();
                }
            }
        }

        dfs(&mut substr, &s, &mut res);
        res
    }
}
// @lc code=end
