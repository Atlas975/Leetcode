/*
 * @lc app=leetcode id=380 lang=rust
 *
 * [380] Insert Delete GetRandom O(1)
 */

// @lc code=start
use std::collections::HashMap;
use rand::Rng;
use rand::thread_rng;

struct RandomizedSet {
    mut map: HashMap<i32, usize>,
    mut vec: Vec<i32>
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {

    fn new() -> Self {
        RandomizedSet {
            map: HashMap::new(),
            vec: Vec::new()
        }
    }

    fn insert(&self, val: i32) -> bool {
        let not_exist = !self.map.contains_key(&val);
        if not_exist {
            self.map.insert(val, self.vec.len());
            self.vec.push(val);
        }
        not_exist
    }

    fn remove(&self, val: i32) -> bool {
        let exist = self.map.contains_key(&val);
        if exist {
            let index = self.map.get(&val).unwrap();
            let last = self.vec.last().unwrap();
            self.map.insert(*last, *index);
            self.vec[*index] = *last;
            self.vec.pop();
            self.map.remove(&val);
        }
        exist

    }

    fn get_random(&self) -> i32 {
        self.vec[thread_rng().gen_range(0, self.vec.len())]
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */
// @lc code=end

