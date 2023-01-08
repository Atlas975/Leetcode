/*
 * @lc app=leetcode id=6 lang=rust
 *
 * [6] Zigzag Conversion
 */

// @lc code=start
impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows == 1 {return s;}
        let (mut i, mut step, end) = (0, 1, num_rows - 1);
        let mut rows = vec![String::new(); num_rows as usize];

        for c in s.chars() {
            rows[i as usize].push(c);

            if i == 0 {
                step = 1
            } else if i == end {
                step = -1;
            }

            i += step;
        }
        rows.join("")
    }
}
// @lc code=end

