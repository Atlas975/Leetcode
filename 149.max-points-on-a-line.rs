/*
 * @lc app=leetcode id=149 lang=rust
 *
 * [149] Max Points on a Line
 */

// @lc code=start

use std::collections::HashMap;
impl Solution {
    pub fn max_points(points: Vec<Vec<i32>>) -> i32 {
        if points.len() < 3 {
            return points.len() as i32;
        }
        let slope = |p1: &Vec<i32>, p2: &Vec<i32>| {
            if p1[0] == p2[0] {
                return std::f64::INFINITY;
            }
            (p1[1] - p2[1]) as f64 / (p1[0] - p2[0]) as f64
        };

        let mut max = 1;
        for i, p1 in points.iter().enumerate() {
            let mut map = HashMap::new();
            for j, p2 in points.iter().enumerate() {
                if i == j {
                    continue;
                }
                let s = slope(p1, p2);
                let count = map.entry(s).or_insert(0);
                *count += 1;
                max = max.max(*count + 1);
            }
        }
        max

    }
}
// @lc code=end

