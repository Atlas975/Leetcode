/*
 * @lc app=leetcode id=48 lang=rust
 *
 * [48] Rotate Image
 */

// @lc code=start
impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let (mut l, mut r) = (0, matrix.len() - 1);
        while l < r {
            for i in 0..(r - l) {
                let tleft = matrix[l][l + i];
                matrix[l][l + i] = matrix[r - i][l];
                matrix[r - i][l] = matrix[r][r - i];
                matrix[r][r - i] = matrix[l + i][r];
                matrix[l + i][r] = tleft;
            }
            l += 1;
            r -= 1;
        }
    }
}
// @lc code=end

