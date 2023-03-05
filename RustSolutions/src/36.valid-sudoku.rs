/*
 * @lc app=leetcode id=36 lang=rust
 *
 * [36] Valid Sudoku
 */

// @lc code=start

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let (mut cols, mut rows, mut grids) = (0u128, 0u128, 0u128);
        board
            .into_iter()
            .enumerate()
            .flat_map(|(r, row)| {
                row.into_iter()
                    .enumerate()
                    .filter(|(_, c)| *c != '.')
                    .map(move |(c, cell)| {
                        let offset = (cell as u8 - b'1') as usize;
                        (
                            1 << (c * 9 + offset),
                            1 << (r * 9 + offset),
                            1 << (((r / 3) * 3 + c / 3) * 9 + offset),
                        )
                    })
            })
            .all(|(rbit, cbit, gbit)| {
                if (cols & cbit) | (rows & rbit) | (grids & gbit) != 0 {
                    return false;
                }
                cols |= cbit;
                rows |= rbit;
                grids |= gbit;
                true
            })
    }
}
// @lc code=end
