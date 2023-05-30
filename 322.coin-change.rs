/*
 * @lc app=leetcode id=322 lang=rust
 *
 * [322] Coin Change
 */

// @lc code=start
use std::collections::HashSet;

impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let coins = coins
            .into_iter()
            .filter(|&c| c <= amount)
            .map(|c| c as usize)
            .collect::<HashSet<_>>();
        if coins.is_empty() {
            return if amount == 0 { 0 } else { -1 };
        }

        let mut dp = vec![i32::MAX; amount as usize + 1];
        let (minc, maxc) = (
            *coins.iter().min().unwrap() as usize,
            *coins.iter().max().unwrap() as usize,
        );
        dp[0] = 0;
        dp[minc] = 1;
        dp[maxc] = 1;

        for a in (minc + 1)..maxc {
            dp[a] = 1 + coins
                .iter()
                .filter(|&&c| c <= a)
                .map(|&c| dp[a - c])
                .min()
                .unwrap();
        }
        for a in (maxc + 1)..=amount as usize {
            dp[a] = 1 + coins.iter().map(|&c| dp[a - c]).min().unwrap();
        }

        if dp[amount as usize + 1] == i32::MAX {
            -1
        } else {
            dp[amount as usize + 1]
        }
    }
}
// @lc code=end
