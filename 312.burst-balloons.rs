/*
 * @lc app=leetcode id=312 lang=rust
 *
 * [312] Burst Balloons
 */

// @lc code=start
impl Solution {
    pub fn max_coins(nums: Vec<i32>) -> i32 {
        let mut nums2 = vec![1];
        nums2.extend(nums.into_iter());
        nums2.push(1);
        let n = nums2.len();
        let mut dp = vec![vec![0; n]; n];
        
        for l in (0..=n - 3).rev() {
            for r in (l + 2)..n {
                let adjprod = nums2[l] * nums2[r];
                dp[l][r] = (l + 1..r)
                    .map(|i| dp[l][i] + (adjprod * nums2[i]) + dp[i][r])
                    .max()
                    .unwrap_or(0);
            }
        }
        dp[0][n - 1]
    }
}
// @lc code=end
≈≈≈≈≈≈