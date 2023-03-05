/*
 * @lc app=leetcode id=45 lang=rust
 *
 * [45] Jump Game II
 */

// @lc code=start
impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        let (mut l, mut r, mut res) = (0, 0, 0);
        let lstidx = nums.len() - 1;

        while r < lstidx {
            let mxjmp = (l..=r).map(|i| i + nums[i] as usize).max().unwrap();
            l = r + 1;
            r = mxjmp;
            res += 1;
        }
        res
    }
}
// @lc code=end
