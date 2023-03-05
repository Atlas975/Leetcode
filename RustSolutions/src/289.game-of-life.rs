/*
 * @lc app=leetcode id=289 lang=rust
 *
 * [289] Game of Life
 */

// @lc code=start
impl Solution {
    pub fn game_of_life(board: &mut Vec<Vec<i32>>) {
        let n = board.len();
        let m = board[0].len();

        fn count_neighbours(board: &Vec<Vec<i32>>, n: usize, m: usize, r: usize, c: usize) -> i32 {
            let coords = vec![
                (r - 1, c - 1),
                (r - 1, c),
                (r - 1, c + 1),
                (r, c - 1),
                (r, c + 1),
                (r + 1, c - 1),
                (r + 1, c),
                (r + 1, c + 1),
            ];

            coords.iter()
                .filter(move |&&(nr, nc)| nr < n && nc < m && board[nr][nc] % 2 == 1)
                .count() as i32
        }


        for r in 0..n {
            for c in 0..m {
                let count = count_neighbours(&board,n,m,r, c);
                if (board[r][c] == 1 && (count == 2 || count == 3)) || (board[r][c] == 0 && count == 3) {
                    board[r][c] |= 2;
                }
            }
        }

        for r in 0..n {
            for c in 0..m {
                board[r][c] >>= 1;
            }
        }
    }
}


// @lc code=end

