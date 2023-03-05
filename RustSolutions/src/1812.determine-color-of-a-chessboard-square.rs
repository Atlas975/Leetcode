/*
 * @lc app=leetcode id=1812 lang=rust
 *
 * [1812] Determine Color of a Chessboard Square
 */

// @lc code=start
impl Solution {
    pub fn square_is_white(coordinates: String) -> bool {
        coordinates.chars().fold(0, |acc, c| acc + c as u8) % 2 == 1
    }
}
// @lc code=end

