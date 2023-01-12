/*
 * @lc app=leetcode id=2248 lang=rust
 *
 * [2248] Intersection of Multiple Arrays
 */

// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn intersection(nums: Vec<Vec<i32>>) -> Vec<i32> {
        let l = nums.len();
        let mut vec = nums.into_iter()
            .flatten()
            .fold(HashMap::new(), |mut map, elt| {
                *map.entry(elt).or_insert(0) += 1;
                map
            })
            .into_iter()
            .filter_map(|(k, v)| if v == l { Some(k) } else { None })
            .collect::<Vec<i32>>();
        vec.sort_unstable();
        vec
    }
}
// @lc code=end

