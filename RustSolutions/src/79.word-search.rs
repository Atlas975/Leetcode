/*
 * @lc app=leetcode id=79 lang=rust
 *
 * [79] Word Search
 */

// @lc code=start
impl Solution {
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let mut board_cpy = board.clone();
        for i in 0..board.len() {
            for j in 0..board[0].len() {
                if Self::dfs(&mut board_cpy, &word, i, j, 0) {
                    return true;
                }
            }
        }
        return false;
    }

    pub fn dfs(board: &mut Vec<Vec<char>>, word: &String, i: usize, j: usize, k: usize) -> bool {
        if
        i<0 || j<0 ||
        i >= board.len() || j >= board[0].len() ||
        board[i][j] != word.chars().nth(k).unwrap()
        {
            return false;
        }
        if k == word.len() - 1 {
            return true;
        }
        board[i][j] = '#';
        let res =
            Self::dfs(board, word, i + 1, j, k + 1)
            || Self::dfs(board, word, i - 1, j, k + 1)
            || Self::dfs(board, word, i, j + 1, k + 1)
            || Self::dfs(board, word, i, j - 1, k + 1);
        board[i][j] = word.chars().nth(k).unwrap();
        res
    }
}
// @lc code=end

