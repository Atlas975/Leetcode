/*
 * @lc app=leetcode id=79 lang=rust
 *
 * [79] Word Search
 */

// @lc code=start
impl Solution {
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let (n, m , wrdle) = (board.len(), board[0].len(), word.len());
        let mut visited = vec![vec![false; m]; n];

    }
}
// @lc code=end

