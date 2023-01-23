/*
 * @lc app=leetcode id=146 lang=rust
 *
 * [146] LRU Cache
 */

// @lc code=start

use std::collections::HashMap;
use std::rc::Rc;
use std::cell::RefCell;


struct Node {
    key: i32,
    value: i32,
    prev: Option<Rc<RefCell<Node>>>,
    next: Option<Rc<RefCell<Node>>>,
}

impl Node {
    fn new(key: i32, value: i32) -> Rc<RefCell<Node>> {
        Rc::new(RefCell::new(Node {
            key,
            value,
            prev: None,
            next: None,
        }))
    }
}

struct LRUCache {
    capacity: i32,
    cache: HashMap<i32, Rc<RefCell<Node>>>,
    head: Option<Rc<RefCell<Node>>>,
    tail: Option<Rc<RefCell<Node>>>,
}

impl LRUCache {

    fn new(capacity: i32) -> Self {
        let left = Node::new(0, 0);
        let right = Node::new(0, 0);
        left.borrow_mut().next = Some(right.clone());
        right.borrow_mut().prev = Some(left.clone());
        
        cache = LRUCache {
            capacity,
            cache: HashMap::new(),
            head: None
            tail: None,
        };

    }

    fn get(&self, key: i32) -> i32 {

    }

    fn put(&self, key: i32, value: i32) {

    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache::new(capacity);
 * let ret_1: i32 = obj.get(key);
 * obj.put(key, value);
 */
// @lc code=end

