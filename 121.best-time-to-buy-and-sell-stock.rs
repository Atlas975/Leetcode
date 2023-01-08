/*
 * @lc app=leetcode id=121 lang=rust
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let profit = prices.iter().enumerate().fold((0, 0), |(profit, min), (i, &price)| {
            if i == 0 {
                (0, price)
            } else {
                (profit.max(price - min), min.min(price))
            }
        });
        profit.0

    }
}
// @lc code=end

