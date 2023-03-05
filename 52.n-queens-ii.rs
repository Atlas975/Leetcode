/*
 * @lc app=leetcode id=52 lang=rust
 *
 * [52] N-Queens II
 */

// @lc code=start
impl Solution {
    pub fn total_n_queens(n: i32) -> i32 {
        fn dfs(r: usize, n: usize, cols: u16, pdiag: u16, ndiag: u16) -> i32 {
            let mut comb = 0;
            for c in 0..n {
                if (cols & (1 << c)) != 0
                    || (pdiag & (1 << (r + c))) != 0
                    || (ndiag & (1 << (r - c + n))) != 0
                {
                    continue;
                }
                if r == n - 1 {
                    return 1;
                }

                comb += dfs(
                    r + 1,
                    n,
                    cols | (1 << c),
                    pdiag | (1 << (r + c)),
                    ndiag | (1 << (r - c + n)),
                );
            }
            comb
        }

        dfs(0, n as usize, 0, 0, 0)
    }
}
// @lc code=end

