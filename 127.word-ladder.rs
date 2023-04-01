/*
 * @lc app=leetcode id=127 lang=rust
 *
 * [127] Word Ladder
 */

// @lc code=start
use std::{
    collections::{HashMap, HashSet, VecDeque},
    mem::swap,
};

impl Solution {
    pub fn ladder_length(begin_word: String, end_word: String, word_list: Vec<String>) -> i32 {
        let mut word_set: HashSet<String> = word_list.into_iter().collect();
        if !word_set.contains(&end_word) {
            return 0;
        }
        let mut bq = VecDeque::from([(1, begin_word.clone())]);
        let mut eq = VecDeque::from([(1, end_word.clone())]);
        let mut bpos = HashMap::from([(begin_word, 1)]);
        let mut epos = HashMap::from([(end_word, 1)]);

        while !bq.is_empty() && !eq.is_empty() {
            for _ in 0..bq.len() {
                let (dist, word) = bq.pop_front().unwrap();
                for (i, c) in word.chars().enumerate() {
                    let (begin, end) = (&word[..i], &word[i + 1..]);
                    for l in ('a'..='z').filter(|&l| l != c) {
                        let nw = format!("{}{}{}", begin, l, end);
                        if let Some(&d) = epos.get(&nw) {
                            return dist + d;
                        }
                        if word_set.contains(&nw){
                            word_set.remove(&nw);
                            bpos.insert(nw.clone(), dist + 1);
                            bq.push_back((dist + 1, nw));
                        }
                    }
                }
            }
            if bq.len() > eq.len() {
                swap(&mut bq, &mut eq);
                swap(&mut bpos, &mut epos);
            }
        }
        0
    }
}
// @lc code=end
