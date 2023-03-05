/*
 * @lc app=leetcode id=295 lang=rust
 *
 * [295] Find Median from Data Stream
 */

// @lc code=start
use std::collections::BinaryHeap;
use std::cmp::Reverse;

struct MedianFinder {
    lmax: BinaryHeap<i32>,
    rmin: BinaryHeap<i32>,
    isEven: bool,
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MedianFinder {

    fn new() -> Self {
        MedianFinder {
            lmax: BinaryHeap::new(),
            rmin: BinaryHeap::new(),
            isEven: true,
        }
    }

    fn add_num(&mut self, num: i32) {
        if self.isEven {
            self.lmax.push(num);
            self.rmin.push(-self.lmax.pop().unwrap());
        } else {
            self.rmin.push(-num);
            self.lmax.push(-self.rmin.pop().unwrap());
        }
        self.isEven = !self.isEven;
    }

    fn find_median(&mut self) -> f64 {
        if self.isEven {
            (self.lmax.peek().unwrap() - self.rmin.peek().unwrap()) as f64 / 2.0
        } else {
            -self.rmin.peek().unwrap() as f64
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * let obj = MedianFinder::new();
 * obj.add_num(num);
 * let ret_2: f64 = obj.find_median();
 */
// @lc code=end

