/*
 * @lc app=leetcode id=121 lang=rust
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        // Functional version
        prices
        .into_iter()
        .fold((0, i32::MAX), |(mxprof, cost), price| match price < cost {
            true => (mxprof, price),
            false => (mxprof.max(price - cost), cost),
        })
        .0

        // // Imperative version
        // let (mut mxprof, mut cost) = (0, prices[0]);
        // for price in prices.into_iter().skip(1) {
        //     if price < cost {
        //         cost = price;
        //     } else {
        //         mxprof = mxprof.max(price - cost);
        //     }
        // }
        // mxprof
    }
}
// @lc code=end
