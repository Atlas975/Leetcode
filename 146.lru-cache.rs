/*
 * @lc app=leetcode id=146 lang=rust
 *
 * [146] LRU Cache
 */

// @lc code=start
use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::{Rc, Weak};

type StrongNode = Rc<RefCell<Node>>;
type WeakNode = Weak<RefCell<Node>>;
macro_rules! option_down {
    ($x:expr) => {
        Some(Rc::downgrade(&$x))
    };
}

#[derive(Debug)]
struct Node {
    key: i32,
    value: i32,
    next: Option<WeakNode>,
    prev: Option<WeakNode>,
}

impl Node {
    fn new(key: i32, value: i32) -> WeakNode {
        Rc::downgrade(&Self::new_strong(key, value))
    }

    fn new_strong(key: i32, value: i32) -> StrongNode {
        Rc::new(RefCell::new(Node {
            key,
            value,
            prev: None,
            next: None,
        }))
    }

    fn update_value(&mut self, value: i32) {
        self.value = value;
    }

    fn get_key(&self) -> i32 {
        self.key
    }
}

#[derive(Debug)]
struct LRUCache {
    capacity: usize,
    cache: HashMap<i32, StrongNode>,
    head: StrongNode,
    tail: StrongNode,
}

impl LRUCache {
    fn new(capacity: i32) -> Self {
        let (head, tail) = (Node::new_strong(0, 0), Node::new_strong(0, 0));
        head.borrow_mut().next = option_down!(&tail);
        tail.borrow_mut().prev = option_down!(&head);

        LRUCache {
            capacity: capacity as usize,
            cache: HashMap::new(),
            head,
            tail,
        }
    }

    fn append(&mut self, node: StrongNode) {
        let (nodelink, nodemut) = (option_down!(&node), node.borrow_mut());
        let prenode = self.tail.borrow().prev.clone();
        nodemut.prev = prenode.clone();
        nodemut.next = option_down!(&self.head);

        if let Some(prenode) = prenode.and_then(|x| x.upgrade()) {
            self.head.borrow_mut().prev = nodelink;
            prenode.borrow_mut().next = nodelink;
        }

        self.cache.insert(nodemut.key, node);
    }

    fn pop(&mut self, key: i32) -> Option<StrongNode> {
        let remnode = match self.cache.get_mut(&key) {
            Some(remnode) => remnode.clone(),
            _ => return None,
        };

        let (left, right) = (remnode.borrow().prev.clone(), remnode.borrow().next.clone());

        if let Some(left) = left.and_then(|x| x.upgrade()) {
            left.borrow_mut().next = right.clone();
        }

        if let Some(right) = right.and_then(|x| x.upgrade()) {
            right.borrow_mut().prev = left.clone();
        }

        self.cache.remove(&key);
        Some(remnode)
    }

    fn get(&mut self, key: i32) -> i32 {
        if let Some(node) = self.cache.get(&key) {
            if let Some(node) = self.pop(key) {
                self.append(node);
                return node.borrow().value;
            } else {
                return -1;
            }
        }
        -1
    }

    fn put(&mut self, key: i32, value: i32) {
        if let Some(node) = self.cache.get(&key) {
            node.borrow_mut().update_value(value);
            self.pop(key);
            self.append(node.clone());
            return;
        }

        let node = Node::new_strong(key, value);
        self.append(node.clone());
        self.cache.insert(key, node);
    }
    // fn put(&mut self, key: i32, value: i32) {
    //     if let Some(node) = self.cache.get(&key) {
    //         node.borrow_mut().update_value(value);
    //         self.pop(key);
    //         self.append(node.clone());
    //         return;
    //     }

    //     let node = Node::new(key, value);
    //     self.append(node.clone());
    //     self.cache.insert(key, node);
    // }
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache::new(capacity);
 * let ret_1: i32 = obj.get(key);
 * obj.put(key, value);
 */
// @lc code=end

