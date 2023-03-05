/*
 * @lc app=leetcode id=2404 lang=rust
 *
 * [2404] Most Frequent Even Element
 */

// @lc code=start
use std::cmp::Reverse;
use std::collections::HashMap;

impl Solution {
    pub fn most_frequent_even(nums: Vec<i32>) -> i32 {
        let mut map = HashMap::new();
        nums.into_iter().filter(|x| x % 2 == 0).for_each(|x| {
            map.entry(x).and_modify(|x| *x += 1).or_insert(1);
        });

        map.into_iter()
            .max_by_key(|&(k, v)| (v, Reverse(k)))
            .unwrap_or((-1, 0))
            .0
    }
}
// @lc code=end
