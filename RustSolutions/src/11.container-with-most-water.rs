/*
 * @lc app=leetcode id=11 lang=rust
 *
 * [11] Container With Most Water
 */

// @lc code=start
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let (mut l, mut r) = (0, height.len() - 1);
        let mut mxarea = 0;
        while l < r {
            if height[l] < height[r] {
                mxarea = mxarea.max(height[l] * (r - l) as i32);
                l += 1;
            } else {
                mxarea = mxarea.max(height[r] * (r - l) as i32);
                r -= 1;
            }
        }
        mxarea
    }
}
// @lc code=end

