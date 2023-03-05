/*
 * @lc app=leetcode id=208 lang=rust
 *
 * [208] Implement Trie (Prefix Tree)
 */

// @lc code=start
use std::collections::HashMap;

struct Trie {
    children: HashMap<char, Trie>,
    is_word: bool,
    refs: i32,
}

impl Trie {
    fn new() -> Self {
        Trie {
            children: HashMap::new(),
            is_word: false,
            refs: 0,
        }
    }

    fn insert(&mut self, word: String) {
        let mut node = self;
        for c in word.chars() {
            node = node.children.entry(c).or_insert(Trie::new());
        }
        node.is_word = true;
    }

    // fn remove(&mut self, word: &str) {
    //     let mut path: Vec<&mut Trie> = Vec::new();
    //     path.push(self);

    //     for c in word.chars() {
    //         if let Some(n) = path[path.len() - 1].children.get_mut(&c) {
    //             path.push(n);
    //         } else {
    //             return;
    //         }
    //     }

    //     let n = path.len();
    //     if !path[n - 1].is_word {
    //         return;
    //     }
    //     path[n - 1].is_word = false;
    //     if path[n - 1].children.len() > 0 {
    //         return;
    //     }

    //     let mut remroot = word.chars().last().unwrap();
    //     for (node, c) in path[0..n - 1].iter_mut().zip(word.chars().rev().skip(1)) {
    //         if node.children.len() > 1 || node.is_word {
    //             node.children.remove(&remroot);
    //             return;
    //         }
    //         remroot = c;
    //     }
    // }

    fn search(&self, word: String) -> bool {
        let mut node = self;
        for c in word.chars() {
            if let Some(n) = node.children.get(&c) {
                node = n;
            } else {
                return false;
            }
        }
        return node.is_word;
    }

    fn starts_with(&self, prefix: String) -> bool {
        let mut node = self;
        for c in prefix.chars() {
            if let Some(n) = node.children.get(&c) {
                node = n;
            } else {
                return false;
            }
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * let obj = Trie::new();
 * obj.insert(word);
 * let ret_2: bool = obj.search(word);
 * let ret_3: bool = obj.starts_with(prefix);
 */
// @lc code=end

