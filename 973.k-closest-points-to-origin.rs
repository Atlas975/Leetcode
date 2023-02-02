/*
 * @lc app=leetcode id=973 lang=rust
 *
 * [973] K Closest Points to Origin
 */

// @lc code=start

use std::collections::BinaryHeap;
use std::cmp::Reverse;
impl Solution {
    pub fn k_closest(points: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let k = k as usize;
        let dist_origin = |p: &Vec<i32>| p[0] * p[0] + p[1] * p[1];
        let minheap = points.iter().map(|p| (dist_origin(p), p)).fold(
            BinaryHeap::with_capacity(k),
            |mut heap, (dist, p)| {
                heap.push(Reverse((dist, p)));
                if heap.len() > k {
                    heap.pop();
                };
                heap
            },
        );
        minheap
            .into_sorted_vec()
        
    }
}
// @lc code=end
