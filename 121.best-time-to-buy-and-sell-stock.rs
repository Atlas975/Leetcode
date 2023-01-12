/*
 * @lc app=leetcode id=121 lang=rust
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        prices
            .into_iter()
            .fold((0, i32::MAX), |(profit, cost), price| {
                (profit.max(price - cost), price.min(cost))
            })
            .0
    }
}
// @lc code=end
