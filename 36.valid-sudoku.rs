/*
 * @lc app=leetcode id=36 lang=rust
 *
 * [36] Valid Sudoku
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut cols = HashMap::new();
        let mut rows = HashMap::new();
        let mut grids = HashMap::new();
        for i in 0..9 {
            for j in 0..9 {
                let c = board[i][j];
                if c == '.' {
                    continue;
                }
                let grid = (i / 3) * 3 + j / 3;
                if cols.contains_key(&(j, c))|| rows.contains_key(&(i, c)) || grids.contains_key(&(grid, c)) {
                    return false;
                }
                cols.insert((j, c), true);
                rows.insert((i, c), true);
                grids.insert((grid, c), true);
            }
        }
        return true;

    }
}
// @lc code=end

