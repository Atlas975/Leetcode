/*
 * @lc app=leetcode id=78 lang=rust
 *
 * [78] Subsets
 */

// @lc code=start
impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        fn dfs(nums: &[i32], path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
            let mut next = path.clone();
            res.push(path);
            for (i, &num) in nums.iter().enumerate() {
                next.push(num);
                dfs(&nums[i + 1..], &mut next, res);
            }
        }

        let mut res = vec![];
        dfs(&nums, &mut vec![], &mut res);
        res
    }
}
// @lc code=end
