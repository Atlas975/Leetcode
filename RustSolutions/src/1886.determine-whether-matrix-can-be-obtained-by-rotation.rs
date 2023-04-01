/*
 * @lc app=leetcode id=1886 lang=rust
 *
 * [1886] Determine Whether Matrix Can Be Obtained By Rotation
 */

// @lc code=start
impl Solution {
    pub fn find_rotation(mut mat: Vec<Vec<i32>>, target: Vec<Vec<i32>>) -> bool {
        let n = mat.len();

        if mat == target {
            return true;
        }
        (0..3).any(|_| {
            for (i, j) in (0..(n / 2)).flat_map(|i| (i..(n - i - 1)).map(move |j| (i, j))) {
                let (tmp, b, r) = (mat[i][j], n - j - 1, n - i - 1);
                mat[i][j] = mat[b][i];
                mat[b][i] = mat[r][b];
                mat[r][b] = mat[j][r];
                mat[j][r] = tmp;
            }
            mat == target
        })
    }
}
// @lc code=end
