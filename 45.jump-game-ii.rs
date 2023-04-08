/*
 * @lc app=leetcode id=45 lang=rust
 *
 * [45] Jump Game II
 */

// @lc code=start
impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        let mut jumps = 0;
        let mut current_jump_end = 0;
        let mut farthest = 0;
        let lstidx = nums.len() - 1;
        while current_jump_end < lstidx {
            let tmp = farthest;
            farthest = (current_jump_end..=tmp)
                .map(|i| i + nums[i] as usize)
                .max()
                .unwrap();
            current_jump_end = tmp + 1;
            jumps += 1;
        }
        jumps
    }
}
// @lc code=end
