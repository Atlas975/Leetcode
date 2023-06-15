/*
 * @lc app=leetcode id=146 lang=rust
 *
 * [146] LRU Cache
 */

// @lc code=start
use std::cell::{Ref, RefCell};
use std::collections::HashMap;
use std::rc::{Rc, Weak};
type StrongNode = Rc<RefCell<Node>>;
type WeakNode = Weak<RefCell<Node>>;
macro_rules! weak_link {
    ($node:expr) => {
        Some(Rc::downgrade($node))
    };
}
macro_rules! upgrade_ref {
    ($node:expr) => {
        $node.clone().unwrap().upgrade().unwrap()
    };
}

struct Node {
    key: i32,
    value: i32,
    next: Option<WeakNode>,
    prev: Option<WeakNode>,
}

impl Node {
    fn new(key: i32, value: i32) -> StrongNode {
        Rc::new(RefCell::new(Node {
            key,
            value,
            prev: None,
            next: None,
        }))
    }
}

struct LRUCache {
    capacity: usize,
    cache: HashMap<i32, StrongNode>,
    head: StrongNode,
    tail: StrongNode,
}

impl LRUCache {
    fn new(capacity: i32) -> Self {
        let (head, tail) = (Node::new(0, 0), Node::new(0, 0));
        head.borrow_mut().next = weak_link!(&tail);
        tail.borrow_mut().prev = weak_link!(&head);

        LRUCache {
            capacity: capacity as usize,
            cache: HashMap::new(),
            head,
            tail,
        }
    }

    fn append(&self, node: StrongNode) {
        let (mut right, mut node_mut) = (self.tail.borrow_mut(), node.borrow_mut());
        let left = upgrade_ref!(right.prev);

        node_mut.prev = weak_link!(&left);
        node_mut.next = weak_link!(&self.tail);
        left.borrow_mut().next = weak_link!(&node);
        right.prev = weak_link!(&node);
    }

    fn pop(&self, node: Ref<Node>) {
        upgrade_ref!(node.prev).borrow_mut().next = node.next.clone();
        upgrade_ref!(node.next).borrow_mut().prev = node.prev.clone();
    }

    fn lru_hit(&mut self, key: &i32) -> Option<StrongNode> {
        let node = match self.cache.get(key) {
            Some(node) => node.clone(),
            None => return None,
        };
        self.pop(node.borrow());
        self.append(node.clone());
        Some(node)
    }

    fn get(&mut self, key: i32) -> i32 {
        match self.lru_hit(&key) {
            Some(node) => node.borrow().value,
            None => -1,
        }
    }

    fn put(&mut self, key: i32, value: i32) {
        if let Some(node) = self.lru_hit(&key) {
            node.borrow_mut().value = value;
            return;
        }

        if self.cache.len() == self.capacity {
            let lru = upgrade_ref!(self.head.borrow().next);
            self.pop(lru.borrow());
            self.cache.remove(&lru.borrow().key);
        }

        let node = Node::new(key, value);
        self.append(node.clone());
        self.cache.insert(key, node);
    }
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache::new(capacity);
 * let ret_1: i32 = obj.get(key);
 * obj.put(key, value);
 */
// @lc code=end

