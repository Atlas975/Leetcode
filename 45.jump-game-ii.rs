/*
 * @lc app=leetcode id=45 lang=rust
 *
 * [45] Jump Game II
 */

// @lc code=start
impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        let (mut l, mut r, mut res) = (0, 0, 0);

        while r < nums.len() - 1 {
            let max_i = (l..=r).map(|i| i + nums[i] as usize).max().unwrap_or(0);
            l = r + 1;
            r = max_i;
            res += 1;
        }
        res
    }
}
// @lc code=end
