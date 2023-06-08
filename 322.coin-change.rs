/*
 * @lc app=leetcode id=322 lang=rust
 *
 * [322] Coin Change
 */

// @lc code=start
use std::collections::HashSet;

impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let coins: Vec<usize> = coins
            .into_iter()
            .filter(|&c| c <= amount)
            .map(|c| c as usize)
            .collect();
        let amount = amount as usize;

        if coins.is_empty() {
            return if amount == 0 { 0 } else { -1 };
        }
        let n = coins.iter().max().unwrap() + 1;
        let mut dp = vec![usize::MAX; n];

        dp[0] = 0;
        dp[n - 1] = 1;
        for &c in &coins {
            for a in c..(n - 1) {
                dp[a] = dp[a].min(1 + dp[a - c]);
            }
        }

        for a in n..=amount {
            dp[a % n] = 1 + coins.iter().map(|&c| dp[(a - c) % n]).min().unwrap();
        }

        println!("{:?}", dp);
        println!("{:?}", amount % n);

        if dp[amount % n] != usize::MAX {
            dp[amount % n] as i32
        } else {
            -1
        }
    }
}
// @lc code=end
