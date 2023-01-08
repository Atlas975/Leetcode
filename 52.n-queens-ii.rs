/*
 * @lc app=leetcode id=52 lang=rust
 *
 * [52] N-Queens II
 */

// @lc code=start

use std::collections::HashSet;

impl Solution {
    pub fn total_n_queens(n: i32) -> i32 {
        let mut cols = HashSet::new();
        let mut pdiag = HashSet::new();
        let mut ndiag = HashSet::new();

        #[inline]
        fn dfs(r: i32) -> i32 {
            let mut res = 0;
            for c in 0..n {
                if cols.contains(&c) || pdiag.contains(&(r + c)) || ndiag.contains(&(r - c)) {
                    continue;
                }

                if (r + 1 == n) {
                    return 1;
                }

                cols.insert(c);
                pdiag.insert(r + c);
                ndiag.insert(r - c);
                res += dfs(r + 1);
                cols.remove(&c);
                pdiag.remove(&(r + c));
                ndiag.remove(&(r - c));
            }
            return res;
        }

        dfs(0)
    }
}
// @lc code=end
