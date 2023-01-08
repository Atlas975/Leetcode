/*
 * @lc app=leetcode id=1886 lang=rust
 *
 * [1886] Determine Whether Matrix Can Be Obtained By Rotation
 */

// @lc code=start
impl Solution {
    pub fn find_rotation(mat: Vec<Vec<i32>>, target: Vec<Vec<i32>>) -> bool {
        let mut mat = mat;
        let n = mat.len();

        let rotate = |mat: &mut Vec<Vec<i32>>| {
            for i in 0..n / 2 {
                for j in i..(n - i - 1) {
                    let tmp = mat[i][j];
                    mat[i][j] = mat[n - j - 1][i];
                    mat[n - j - 1][i] = mat[n - i - 1][n - j - 1];
                    mat[n - i - 1][n - j - 1] = mat[j][n - i - 1];
                    mat[j][n - i - 1] = tmp;
                }
            }
        };

        for _ in 0..4 {
            if mat == target {
                return true;
            }
            rotate(&mut mat);
        }
        false

    }
}
// @lc code=end

