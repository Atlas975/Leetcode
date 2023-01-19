/*
 * @lc app=leetcode id=994 lang=rust
 *
 * [994] Rotting Oranges
 */

// @lc code=start
use itertools::iproduct;
use std::collections::VecDeque;
impl Solution {

    pub fn oranges_rotting(grid: Vec<Vec<i32>>) -> i32 {
        let mut grid = grid;
        let (n, m) = (grid.len(), grid[0].len());
        let (mut fresh, mut time) = (0, 0);
        let mut q = VecDeque::new();

        for (r, c) in iproduct!(0..n, 0..m) {
            if grid[r][c] == 1 {
                fresh += 1;
            } else if grid[r][c] == 2 {
                q.push_back((r, c));
            }
        }




        let expand = move |r, c| {
            if grid[r][c] == 1 {
                grid[r][c] = 2;
                q.push_back((r, c));
                return 1;
            }
            0
        };

        while !q.is_empty() && fresh > 0 {
            let qlen = q.len();
            for _ in 0..qlen {
                let (r, c) = q.pop_front().unwrap();
                fresh -= if r > 0 { expand(r - 1, c) } else { 0 }
                    + if r < n - 1 { expand(r + 1, c) } else { 0 }
                    + if c > 0 { expand(r, c - 1) } else { 0 }
                    + if c < m - 1 { expand(r, c + 1) } else { 0 };
            }
            time += 1;
        }

        if fresh > 0 {
            -1
        } else {
            time
        }
    }
}
// @lc code=end

