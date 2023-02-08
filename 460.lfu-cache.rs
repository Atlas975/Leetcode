/*
 * @lc app=leetcode id=460 lang=rust
 *
 * [460] LFU Cache
 */

// @lc code=start
use std::cell::RefCell;
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

struct OrderedDict {
    cache: HashMap<i32, StrongNode>,
    head: StrongNode,
    tail: StrongNode,
}

impl OrderedDict {
    fn new() -> Self {
        let (head, tail) = (Node::new(0, 0), Node::new(0, 0));
        head.borrow_mut().next = weak_link!(&tail);
        tail.borrow_mut().prev = weak_link!(&head);

        OrderedDict {
            cache: HashMap::new(),
            head,
            tail,
        }
    }

    fn append(&mut self, node: StrongNode) {
        let (mut tmut, mut nmut) = (self.tail.borrow_mut(), node.borrow_mut());
        let last = upgrade_ref!(tmut.prev);

        last.borrow_mut().next = weak_link!(&node);
        nmut.prev = weak_link!(&last);
        nmut.next = weak_link!(&self.tail);
        tmut.prev = weak_link!(&node);
        self.cache.insert(nmut.key, node.clone());
    }

    fn pop(&mut self, key: i32) -> i32 {
        let node = self.cache.remove(&key).unwrap();
        let node = node.borrow();
        upgrade_ref!(node.prev).borrow_mut().next = node.next.clone();
        upgrade_ref!(node.next).borrow_mut().prev = node.prev.clone();
        node.value
    }

    fn lru_pop(&mut self) -> i32 {
        let lru_key = upgrade_ref!(self.head.borrow().next).borrow().key;
        self.pop(lru_key);
        lru_key
    }

    fn insert(&mut self, key: i32, value: i32) {
        let node = match self.cache.get(&key) {
            Some(node) => node.clone(),
            None => {
                self.append(Node::new(key, value));
                return;
            }
        };
        node.borrow_mut().value = value;
        self.pop(key);
        self.append(node);
    }

    fn is_empty(&self) -> bool {
        self.cache.is_empty()
    }
}

struct LFUCache {
    capacity: usize,
    f_k_v: HashMap<usize, OrderedDict>,
    k_f: HashMap<i32, usize>,
    minf: usize,
}

impl LFUCache {
    fn new(capacity: i32) -> Self {
        LFUCache {
            capacity: capacity as usize,
            f_k_v: HashMap::new(),
            k_f: HashMap::new(),
            minf: 0,
        }
    }

    fn update(&mut self, key: i32, freq: usize, new_val: i32) {
        self.f_k_v
            .entry(freq + 1)
            .or_insert_with(OrderedDict::new)
            .insert(key, new_val);
        self.k_f.insert(key, freq + 1);

        if self.f_k_v.get(&freq).unwrap().is_empty() {
            self.f_k_v.remove(&freq);
            if self.minf == freq {
                self.minf += 1;
            }
        }
    }

    fn get(&mut self, key: i32) -> i32 {
        let freq = match self.k_f.get(&key) {
            Some(&freq) => freq,
            None => return -1,
        };
        let value = self.f_k_v.get_mut(&freq).unwrap().pop(key);
        self.update(key, freq, value);
        value
    }

    fn put(&mut self, key: i32, value: i32) {
        if let Some(&freq) = self.k_f.get(&key) {
            self.f_k_v.get_mut(&freq).unwrap().pop(key);
            self.update(key, freq, value);
            return;
        }

        self.k_f.insert(key, 1);
        self.f_k_v
            .entry(1)
            .or_insert_with(OrderedDict::new)
            .insert(key, value);

        if self.k_f.len() > self.capacity {
            let lru_key = self.f_k_v.get_mut(&self.minf).unwrap().lru_pop();
            self.k_f.remove(&lru_key);
        }
        self.minf = 1;
    }
}
/**
 * Your LFUCache object will be instantiated and called as such:
 * let obj = LFUCache::new(capacity);
 * let ret_1: i32 = obj.get(key);
 * obj.put(key, value);
 */
// @lc code=end

