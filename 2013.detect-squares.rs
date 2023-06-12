/*
 * @lc app=leetcode id=2013 lang=rust
 *
 * [2013] Detect Squares
 */

// @lc code=start
use std::collections::HashMap;

#[derive(Default)]
struct DetectSquares {
    horiz_mp: HashMap<i32, HashMap<i32, i32>>,
    verti_mp: HashMap<i32, HashMap<i32, i32>>,
}

impl DetectSquares {
    fn new() -> Self {
        Default::default()
    }

    fn point_increment(map: &mut HashMap<i32, HashMap<i32, i32>>, k1: i32, k2: i32) {
        map.entry(k1)
            .or_insert(HashMap::new())
            .entry(k2)
            .and_modify(|v| *v += 1)
            .or_insert(1);
    }

    fn add(&mut self, point: Vec<i32>) {
        let (x, y) = (point[0], point[1]);
        Self::point_increment(&mut self.horiz_mp, x, y);
        Self::point_increment(&mut self.verti_mp, y, x);
    }

    fn count(&self, point: Vec<i32>) -> i32 {
        let mut res = 0;
        let (x1, y1) = (point[0], point[1]);
        let (horiz_1, verti_1) = match (self.verti_mp.get(&y1), self.horiz_mp.get(&x1)) {
            (Some(h), Some(v)) => (h, v),
            _ => return 0,
        };

        for (x2, p2f) in horiz_1 {
            let dif = x1 - x2; // side length
            let verti_2 = match self.horiz_mp.get(&(x2)) {
                Some(p2_verti) => p2_verti,
                None => continue,
            };

            if let (Some(p3f), Some(p4f)) = (verti_1.get(&(y1 - dif)), verti_2.get(&(y1 - dif))) {
                res += p2f * p3f * p4f;
            }
            if let (Some(p3f), Some(p4f)) = (verti_1.get(&(y1 + dif)), verti_2.get(&(y1 + dif))) {
                res += p2f * p3f * p4f;
            }
        }
        res - (2 * horiz_1.get(&x1).unwrap_or(&0).pow(3))
    }
}
/**
 * Your DetectSquares object will be instantiated and called as such:
 * let obj = DetectSquares::new();
 * obj.add(point);
 * let ret_2: i32 = obj.count(point);
 */
// @lc code=end

