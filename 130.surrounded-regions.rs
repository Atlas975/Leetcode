/*
 * @lc app=leetcode id=130 lang=rust
 *
 * [130] Surrounded Regions
 */

// @lc code=start
impl Solution {
    pub fn solve(board: &mut Vec<Vec<char>>) {
        let (n, m) = (board.len(), board[0].len());

        fn capture(board: &mut Vec<Vec<char>>, i: usize, j: usize) {
            if board[i][j] != 'O' {
                return;
            }

            board[i][j] = 'C';
            if i > 0 {
                capture(board, i -1, j);
            }
            if j > 0 {
                capture(board, i, j -1);
            }
            if i < board.len() - 1 {
                capture(board, i + 1, j);
            }
            if j < board[0].len() - 1 {
                capture(board, i, j + 1);
            }
        }

        for r in 0..n {
            capture( board, r, 0);
            capture( board, r, m - 1);
        }

        for c in 0..m {
            capture(board, 0, c);
            capture(board, n - 1, c);
        }

        board.iter_mut().flatten().for_each(|x| {
            if *x == 'O' {
                *x = 'X';
            } else if *x == 'C' {
                *x = 'O';
            }
        });
    }
}
// @lc code=end
