/*
 * @lc app=leetcode id=1351 lang=rust
 *
 * [1351] Count Negative Numbers in a Sorted Matrix
 */

// @lc code=start
impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let mut count = 0;
        for row in grid {
            for num in row {
                if num < 0 {
                    count += 1;
                }
            }
        }
        count
    }
}
// @lc code=end

