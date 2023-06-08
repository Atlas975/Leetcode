/*
 * @lc app=leetcode id=211 lang=rust
 *
 * [211] Design Add and Search Words Data Structure
 */

// @lc code=start
use std::collections::{HashMap, VecDeque};

#[derive(Default)]
struct Trie {
    children: HashMap<char, Trie>,
}

#[derive(Default)]
struct WordDictionary {
    triemp: HashMap<usize, Trie>,
}

impl WordDictionary {
    fn new() -> Self {
        WordDictionary::default()
    }

    fn add_word(&mut self, word: String) {
        let mut node = self.triemp.entry(word.len()).or_insert(Trie::default());
        for c in word.chars() {
            node = node.children.entry(c).or_insert(Trie::default());
        }
    }

    fn search(&self, word: String) -> bool {
        let node = match self.triemp.get(&word.len()) {
            Some(node) => node,
            None => return false,
        };
        let mut s = VecDeque::from([(0, node)]);
        let word = word.chars().collect::<Vec<char>>();

        while let Some((i, node)) = s.pop_back() {
            if i == word.len() {
                return true;
            }
            
            if word[i] == '.' {
                s.extend(node.children.iter().map(|(_, child)| (i + 1, child)));
            } else if let Some(child) = node.children.get(&word[i]) {
                s.push_back((i + 1, child));
            }
        }
        false
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * let obj = WordDictionary::new();
 * obj.add_word(word);
 * let ret_2: bool = obj.search(word);
 */
// @lc code=end

