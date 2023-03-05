/*
 * @lc app=leetcode id=56 lang=rust
 *
 * [56] Merge Intervals
 */

// @lc code=start


impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        intervals.sort_unstable_by_key(|a| a[0]);

        let (mut min, mut max) = (intervals[0][0], intervals[0][1]);
        let mut ret = Vec::new();

        for item in &intervals[1..] {
            if max < item[0] {
                ret.push(vec![min, max]);
                min = item[0];
            }

            min = min.min(item[0]);
            max = max.max(item[1]);
        }

        ret.push(vec![min, max]);
        ret
    }
}
// @lc code=end

