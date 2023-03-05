/*
 * @lc app=leetcode id=36 lang=rust
 *
 * [36] Valid Sudoku
 */

// @lc code=start
impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let (mut cols, mut rows, mut grids) = ([0u16; 9], [0u16; 9], [0u16; 9]);

        for r in 0..9 {
            for c in (0..9).filter(|&c| board[r][c] != '.') {

                let tile = 1 << (board[r][c] as u8 - b'1');
                let g = r - r % 3 + c / 3;

                if tile & (cols[c] | rows[r] | grids[g]) != 0 {
                    return false;
                }
                cols[c] |= tile;
                rows[r] |= tile;
                grids[g] |= tile;
            }
        }
        true
    }
}
// @lc code=end
