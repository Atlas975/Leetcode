/*
 * @lc app=leetcode id=1046 lang=rust
 *
 * [1046] Last Stone Weight
 */

// @lc code=start
use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut stoneheap = stones.iter().fold(
            BinaryHeap::with_capacity(stones.len()),
            |mut heap, &stone| {
                heap.push(Reverse(stone));
                heap
            },
        );
        while stoneheap.len() > 1 {
            let (Reverse(stone1), Reverse(stone2)) = (stoneheap.pop().unwrap(), stoneheap.pop().unwrap());
            if stone1 != stone2 {
                stoneheap.push(Reverse(stone1 - stone2));
            }
        }
        stoneheap.pop().unwrap_or(Reverse(0)).0

    }
}
// @lc code=end

