/*
 * @lc app=leetcode id=417 lang=rust
 *
 * [417] Pacific Atlantic Water Flow
 */

// @lc code=start
impl Solution {
    pub fn pacific_atlantic(heights: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let (n, m) = (heights.len(), heights[0].len());
        if n == 0 || m == 0 {
            return vec![];
        }

        self

        for row in 0..n {
            bfs(row, 0, &mut pac);
            bfs(row, m - 1, &mut atc);
        }
        for col in 0..m {
            bfs(0, col, &mut pac);
            bfs(n - 1, col, &mut atc);
        }
        return pac.intersection(&atc).cloned().collect();
    }

    pub fn bfs(r: usize, c: usize, visited: &mut HashSet<(usize, usize)>) {
        visited.insert((r, c));
        let node = heights[r][c];
        for (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)].iter() {
            let (nr, nc) = (r as i32 + dr, c as i32 + dc);
            if nr >= 0
                && nr < n as i32
                && nc >= 0
                && nc < m as i32
                && !visited.contains(&(nr as usize, nc as usize))
                && heights[nr as usize][nc as usize] >= node
            {
                bfs(nr as usize, nc as usize, visited);
            }
        }
    }
}
// @lc code=end
