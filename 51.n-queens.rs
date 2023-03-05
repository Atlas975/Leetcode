/*
 * @lc app=leetcode id=51 lang=rust
 *
 * [51] N-Queens
 */

// @lc code=start
impl Solution {
    pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
        let mut res = vec![];

        fn dfs(
            r: usize,
            path: &mut Vec<String>,
            cols: u16,
            pdiag: u16,
            ndiag: u16,
            res: &mut Vec<Vec<String>>,
            n: usize,
        ) {
            for c in 0..n {
                if (cols & (1 << c)) != 0
                    || (pdiag & (1 << (r + c))) != 0
                    || (ndiag & (1 << (r - c + n))) != 0
                {
                    continue;
                }
                if r == n - 1 {
                    path.push(format!("{}Q{}", ".".repeat(c), ".".repeat(n - c - 1),));
                    res.push(path.clone());
                    path.pop();
                    return;
                }

                path.push(format!("{}Q{}", ".".repeat(c), ".".repeat(n - c - 1),));
                dfs(
                    r + 1,
                    path,
                    cols | (1 << c),
                    pdiag | (1 << (r + c)),
                    ndiag | (1 << (r - c + n)),
                    res,
                    n,
                );
                path.pop();
            }
        }

        dfs(0, &mut vec![], 0, 0, 0, &mut res, n as usize);
        res
    }
}
// @lc code=end

