/*
 * @lc app=leetcode id=54 lang=rust
 *
 * [54] Spiral Matrix
 */

// @lc code=start
impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let (mut t, mut b) = (0, matrix.len());
        let (mut l, mut r) = (0, matrix[0].len());
        let mut res = vec![];
        
        while l < r && t < b {
            res.extend(matrix[t][l..r].iter());
            t += 1;
            res.extend((t..b).map(|i| matrix[i][r - 1]));
            r -= 1;
            if l == r || t == b {
                return res;
            }
            res.extend(matrix[b - 1][l..r].iter().rev());
            b -= 1;
            res.extend((t..b).map(|i| matrix[i][l]).rev());
            l += 1;
        }
        res
    }
}
// @lc code=end

